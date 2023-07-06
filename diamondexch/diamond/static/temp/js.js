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
