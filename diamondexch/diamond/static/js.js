const input = document.querySelectorAll(".main_form_input"),
button = document.querySelector(".otp_button");

//iterate iver all inouts
input.forEach((input, index1) => {
    input.addEventListener("keyup", () => {
      //this code gets the current input element and stores it in the current Input variable 
      //this is codes gets the next sibling elemnt of the current input elemnt and stores it in the next

 const currentInput = input,
  nextInput = input.nextElementSibling,
  prevInput = input.previousElementSibling;

  //if the value has more then one charater then clear it
   if (currentInput.value.length > 1){
    currentInput.value = "";
    return;
   }
   if(nextInput && nextInput.hasAttribute("disabled") && currentInput.value !== ""){
    nextInput.removeAttribute("disabled");
    nextInput.focus();
   }
    });
});

//focus the first input which index is 0 window load
window.addEventListener("load", () => input[0].focus());


const form = document.getElementById('form');
const phone = document.getElementById('phone-no');
// const password = document.getElementById('password-user');
 

form.addEventListener('submit', e => {
  console.log(e.target);
e.preventDefault();

validateInputs();
});

const setError = (element, message) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerHTML = message;
    inputControl.classList.add('error');
    inputControl.classList.remove('sucess')
}

const setSuccess = element => {
   const inputControl = element.parentElement;
   const errorDisplay = inputControl.querySelector(".error");

   errorDisplay.innerHTML = '';
   inputControl.classList.add('success');
   inputControl.classList.remove('error');
};



const validateInputs = () => {
  const phoneValue = phone.value.trim();
  // const passwordValue = password.value.trim();


  
  if(phoneValue === ""){
    setError(phone, "(phone no. is required)");
  }else if(phoneValue.length < 10){
   setError(phone, '(10 digital reuired)');
  }else if(phoneValue.length >=11){
     setError(phone, "(10 digit phone no.)")
  }else{
    setSuccess(phone);
  }


  // if(passwordValue === ""){
  //   setError(password, "(password is required)");
  // }else if(passwordValue.length < 8){
  //  setError(password, '(password rewuied 8 charecter)');
  // }else{
  //    setSuccess(password);
  // }


};