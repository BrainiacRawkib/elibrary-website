import json
import stripe

from django.shortcuts import render, reverse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.conf import settings
from django.http import JsonResponse, HttpResponse

from .donation_choices import choices, interval, interval_count, donate_type

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
webhook_secret = settings.DJSTRIPE_WEBHOOK_SECRET


class SuccessView(TemplateView):
    template_name = 'donations/successful.html'
    extra_context = {'title': 'Donation Successful'}


class ErrorView(TemplateView):
    template_name = 'donations/canceled.html'
    extra_context = {'title': 'Error Occurred'}


def donors(request):
    # customers = stripe.Event.list()
    # d = [i.data.object for i in customers.data]
    customers = stripe.checkout.Session.list(expand=['data.customer'], limit=50)
    # customers = stripe.checkout.Session.list(expand=['data.customer'], limit=5)
    # d = [i.customer for i in customers.data if i.payment_status == 'paid']
    d = [i.customer for i in customers.data]
    context = {
        'donors': d,
        'title': 'Donors'
    }
    return render(request, 'donations/donors.html', context)


def donate(request):
    context = {
        'donate_type': donate_type,
        'choices': choices,
        'interval': interval,
        'interval_count': interval_count
    }
    return render(request, 'donations/checkout.html', context)


@require_POST
@csrf_exempt
def recurring(request):
    data = json.loads(request.body)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'unit_amount': int(data['amount']) * 100,
                'product': 'prod_HjpuaRz5pbWXBY',
                'recurring': {
                    'interval': data['interval'],
                    'interval_count': int(data['interval_count'])
                }
            },
            'quantity': 1
        }],
        mode='subscription',
        success_url=request.build_absolute_uri(reverse('donations:successful')) + '?session_id={''CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('donations:error')),
    )
    return JsonResponse(session.id, safe=False)


@require_POST
@csrf_exempt
def one_time(request):
    data = json.loads(request.body)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        submit_type='donate',
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product': 'prod_HjpuaRz5pbWXBY',
                'unit_amount': int(data['amount']) * 100,
            },
            'quantity': 1
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('donations:successful')) + '?session_id={''CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('donations:error')),
    )
    return JsonResponse(session.id, safe=False)


@csrf_exempt
def checkout_session(request):
    data = json.loads(request.body)
    if data['donate_type'] == 'recurring':
        recurring(request)
    else:
        one_time(request)


@csrf_exempt
def get_session(request):
    session = stripe.checkout.Session.retrieve(
        request.GET['session_id'],
        expand=['payment_intent']
    )
    return JsonResponse(session)


@csrf_exempt
def webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    if event['type'] == "checkout.session.completed":
        session = event['data']['object']
    return HttpResponse(status=200)
