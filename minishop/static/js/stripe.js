function buy(id) {
        var stripe = Stripe(Publishable_key);
        url = '/buy/'+id
        fetch(url, {method: 'GET'})
        .then(response => response.json())
        .then(session => stripe.redirectToCheckout({ sessionId: session.id }))
};