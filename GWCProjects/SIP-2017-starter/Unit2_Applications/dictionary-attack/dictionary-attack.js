var wordsList = [];

function init() {
  // Load the words from the dictionary text file to wordsList
  var wordsFile = "https://raw.githubusercontent.com/GirlsFirst/SIP-2017/master/Unit2_Applications/dictionary-attack/dictionary.txt?token=ADcVhZjRMd86ZdhPE2jVvIaJdQdzLA6Yks5YvvVSwA%3D%3D";
  $.get(wordsFile, function(data) {
    document.getElementById("btnSubmit").disabled = true;
    wordsList = data.split('\n');
    document.getElementById("btnSubmit").disabled = false;
  });
}

window.onload = init;

/* ADD YOUR CODE BELOW */

function checkPassword() {

  var pw= document.getElementById("pw").value.toLowerCase();
  var i=0;

  for(i; i<wordsList.length; i++) {
    if(pw==wordsList[i]) {
      console.log("weak password");
      break;
    }
  }
  if(pw!=wordsList[i]) {
    console.log("strong password");
  }
}
