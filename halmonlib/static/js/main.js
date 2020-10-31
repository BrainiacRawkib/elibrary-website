// $("input[type='button']").on("change", function() {
//   var fileName = $(this).val().split("\\").pop();
//   $(this).siblings("label[for=id_logo]").addClass("selected").html(fileName);
// });

// $("input[type='button']").on("change", function() {
//   var fileName = $(this).val().split("\\").pop();
//   $(this).siblings(".requiredField").addClass("selected").html(fileName);
// });

// $("input[type='button']").on("change", function() {
//   var fileName = $(this).val().split("\\").pop();
//   $(this).siblings("label[for=id_logo]").addClass("selected").html(fileName);
// });

setTimeout(function () {
    $('#alert-message').fadeOut('slow')
}, 4000)

$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();
})