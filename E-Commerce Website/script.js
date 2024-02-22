document.addEventListener("DOMContentLoaded", function() {
    const checkoutButton = document.querySelector("#checkout-button");
    const paymentForm = document.querySelector("#payment-form");

    checkoutButton.addEventListener("click", function() {
        paymentForm.style.display = "block";
    });

    const paymentDetailsForm = document.querySelector("#payment-details");

    paymentDetailsForm.addEventListener("submit", function(event) {
        event.preventDefault();

        const nameInput = document.querySelector("#name");
        const mobileInput = document.querySelector("#mobile");
        const addressInput = document.querySelector("#address");
        const cardNumberInput = document.querySelector("#card-number");
        const expirationDateInput = document.querySelector("#expiration-date");
        const cvvInput = document.querySelector("#cvv");

        const name = nameInput.value;
        const mobile = mobileInput.value;
        const address = addressInput.value;
        const cardNumber = cardNumberInput.value;
        const expirationDate = expirationDateInput.value;
        const cvv = cvvInput.value;
        paymentDetailsForm.reset();
        paymentForm.style.display = "none";

    document.getElementById("name").addEventListener("input", function() {
        this.value = this.value.replace(/[^a-zA-Z ]/g, "");
      });
  

      document.getElementById("mobile").addEventListener("input", function() {
        this.value = this.value.replace(/[^0-9]/g, "").slice(0, 10);
      });
  
 
      document.getElementById("card-number").addEventListener("input", function() {
        this.value = this.value.replace(/[^0-9]/g, "").slice(0, 16);
      });
  
      document.getElementById("expiration-date").addEventListener("input", function() {
        this.value = this.value.replace(/\D/g, "");
        if (this.value.length > 2) {
          this.value = this.value.slice(0, 2) + "/" + this.value.slice(2, 4);
        }
      });
  
      document.getElementById("cvv").addEventListener("input", function() {
        this.value = this.value.replace(/[^0-9]/g, "").slice(0, 3);
      });
    });
});
