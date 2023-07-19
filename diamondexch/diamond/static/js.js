const inputs = document.querySelectorAll(".main_form_input"),
button = document.querySelector(".otp_button");

// iterate iver all inouts
inputs.forEach((input, index1) => {
    input.addEventListener("keyup", (e) => {
      // this code gets the current input element and stores it in the current Input variable 
      // this is codes gets the next sibling elemnt of the current input elemnt and stores it in the next

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
 //if backspace key is passed
 if (e.key === "Backspace"){
  console.log(inputs);
  inputs.forEach((input, index2) => {
   if (index1 <= index2 && prevInput){
    input.setAttribute("disabled", true);
    currentInput.value = "";
    prevInput.focus();
   }
  });
 }
    });
});

//focus the first input which index is 0 window load
window.addEventListener("load", () => inputs[0].focus());


const form = document.getElementById('form');
const phone = document.getElementById('phone-no');
// const password = document.getElementById('password-user');
 

form.addEventListener('submit', e => {
  console.log(e.target);
// e.preventDefault();

// validateInputs();
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


  const regex = /^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$/gm;

  // const str = `+91-9123654780`;
  let m;

  // while ((m = regex.exec(phoneValue)) !== null) {
  //     // This is necessary to avoid infinite loops with zero-width matches
  //     if (m.index === regex.lastIndex) {
  //         regex.lastIndex++;
  //     }
      
  //     // The result can be accessed through the `m`-variable.
  // }
  

  // if(phoneValue === ""){
  //   setError(phone, "(Empty Input)");
  // }else if(phoneValue.length < 10){
  //  setError(phone, "(Input Length less than 10)");
  // }else if(m[0] != phoneValue) {
  //   setError(phone, "(Invalid Phone Number)");
  // }
  // else {
  //   setSuccess(phone);
  // }
  // setSuccess(phone);


  // if(passwordValue === ""){
  //   setError(password, "(password is required)");
  // }else if(passwordValue.length < 8){
  //  setError(password, '(password rewuied 8 charecter)');
  // }else{
  //    setSuccess(password);
  // }


};