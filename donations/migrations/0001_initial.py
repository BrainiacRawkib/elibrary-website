# Generated by Django 2.2 on 2020-10-11 03:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.BooleanField(default=False)),
                ('amount', models.PositiveIntegerField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donors', to='account.Profile')),
            ],
            options={
                'verbose_name_plural': 'Donors',
            },
        ),
    ]
