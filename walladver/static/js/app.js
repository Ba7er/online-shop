$(document).ready(function(){
var stripe = Stripe('pk_test_5fhB0Rxt2FVGATK0PjDlCTNX00PYVIaqsT');
var elements = stripe.elements();

// Add an instance of the card Element into the `card-element` <div>.
var style = {
  base: {
    // Add your base input styles here. For example:
    fontSize: '16px',
    color: "#32325d",
  }
};

// Create an instance of the card Element.
var card = elements.create('cardNumber', {style: style});

// Add an instance of the card Element into the `card-element` <div>.
card.mount('#card-number');

var cvc = elements.create('cardCvc', {style: style});

// Add an instance of the card Element into the `card-element` <div>.
cvc.mount('#cvv-number');

var exp = elements.create('cardExpiry', {style: style});

// Add an instance of the card Element into the `card-element` <div>.
exp.mount('#exp-date');

// Submit
$('#payment-submit').on('click', function(e){
  e.preventDefault();
  var cardData = {
    'name': $('#name').val()
  };
  stripe.createToken(card, cardData).then(function(result) {
    // console.log(result);
    if(result.error && result.error.message){
      // alert(result.error.message);
    }else{
      // alert(result.token.id);
      stripeTokenHandler(result.token);
    }
  });
});

function stripeTokenHandler(token) {
  // Insert the token ID into the form so it gets submitted to the server
  var form = document.getElementById('payment-form');
  var hiddenInput = document.createElement('input');
  hiddenInput.setAttribute('type', 'hidden');
  hiddenInput.setAttribute('name', 'stripeToken');
  hiddenInput.setAttribute('value', token.id);
  form.appendChild(hiddenInput);

  // Submit the form
  form.submit();
}
});
