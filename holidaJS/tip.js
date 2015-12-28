
function calculateTip(amount, rating) {
  var result = 0;
  if(rating.toLowerCase() == 'terrible') {
    result = amount;
  }
  else if(rating.toLowerCase() == 'poor') {
    result = Math.ceil(amount*0.05);
  }
  else if(rating.toLowerCase() == 'good') {
    result = Math.ceil(amount*0.1);
  }
  else if(rating.toLowerCase() == 'great') {
    result = Math.ceil(amount*0.15);
  }
  else if(rating.toLowerCase() == 'excellent') {
    result = Math.ceil(amount*0.2);
  }
  else{
    result = "Rating not recognised";
  }
return result
}
