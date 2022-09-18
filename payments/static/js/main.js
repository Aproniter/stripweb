function add_to_cart(item_id){
  fetch("/add_to_cart/"+ item_id)
  .then((res) => {
    console.log(res);
  })
  .finally(
    setTimeout(function(){
      window.location.reload();
    }, 500)
  );
};

function del_from_cart(item_id){
  fetch("/del_from_cart/"+ item_id)
  .then((res) => {
    console.log(res);
  })
  .finally(
    setTimeout(function(){
      window.location.reload();
    }, 500)
    
  );
}

function pay(item_id=NaN, order_id=NaN){
  fetch("/config/")
  .then((result) => { return result.json(); })
  .then((data) => {
  const stripe = Stripe(data.publicKey);
  const order = order_id ? (order_id + "?order=1") : item_id
  fetch("/buy/" + order)
  .then((result) => { return result.json(); })
  .then((data) => {
    console.log(data);
    return stripe.redirectToCheckout({sessionId: data.sessionId})
  })
  .then((res) => {
    console.log(res);
  });
    });
}



