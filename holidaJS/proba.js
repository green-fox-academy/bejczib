function Robot() {
  this.inventory = ['thank', 'you', 'for', 'teaching', 'me', 'i', 'already', 'know', 'the', 'word', "don't", 'understand', 'input'];
  this.learnWord = function(word) {
  if (/[a-zA-Z]/.test(word) == false) {
  return 'I do not understand the input';
  }
  else if(this.inventory.indexOf(word.toLowerCase()) < 0) {
    this.inventory.push(word);
    return 'Thank you for teaching me ' + word;
  }
  else if(this.inventory.indexOf(word.toLowerCase()) > -1) {
    return 'I already know the word ' + word;
  }
  }
}

var alma = new Robot();
console.log(alma.learnWord('123'));
