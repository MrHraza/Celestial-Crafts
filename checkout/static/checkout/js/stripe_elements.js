const stripe = Stripe('{{ stripe_publishable_key }}');
const clientSecret = '{{ client_secret }}';

const appearance = {
    theme: 'flat',
    variables: { colorPrimaryText: '#262626' }
};

const elements = stripe.elements({ clientSecret, appearance });
const paymentElement = elements.create('payment');
paymentElement.mount('#payment-element');


const form = document.getElementById('payment-form');
form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const { error } = await stripe.confirmPayment({
        elements,
        confirmParams: {
            return_url: window.location.origin + "{% url 'order_success' %}",
        },
    });

    if (error) {
        console.log(error.message);
    }
});