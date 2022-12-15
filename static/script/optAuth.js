const firebaseConfig = {
  apiKey: "AIzaSyAFjK9eeI1AZ-sv5ZleSyURm7_yL7vSTJs",
  authDomain: "policefeedbacksystem.firebaseapp.com",
  projectId: "policefeedbacksystem",
  storageBucket: "policefeedbacksystem.appspot.com",
  messagingSenderId: "716265043554",
  appId: "1:716265043554:web:3f4a2e9c2f89ae445e033b"
};

firebase.initializeApp(firebaseConfig);
render();
function render() {
  window.recaptchaVerifier = new firebase.auth.RecaptchaVerifier(
    "recaptcha-container"
  );
  recaptchaVerifier.render();
}
var d;
var c;
var a;
var sa;
var sc;
var sd;
// function for send message
function phoneAuth() {
  var number = document.getElementById("number").value;
  d = document.getElementById("number").value;
  
  firebase
    .auth()
    .signInWithPhoneNumber(number, window.recaptchaVerifier)
    .then(function (confirmationResult) {
      window.confirmationResult = confirmationResult;
      coderesult = confirmationResult;
      document.getElementById("sender").style.display = "none";
      document.getElementById("verifier").style.display = "block";
    })
    .catch(function (error) {
      alert(error.message);
    });
}
// function for code verify
function codeverify() {
  var code = document.getElementById("verificationcode").value;
  coderesult
    .confirm(code)
    .then(function () {
      document.getElementsByClassName("p-conf")[0].style.display = "block";
      document.getElementsByClassName("n-conf")[0].style.display = "none";
    })
    .catch(function () {
      document.getElementsByClassName("p-conf")[0].style.display = "none";
      document.getElementsByClassName("n-conf")[0].style.display = "block";
    });
}


