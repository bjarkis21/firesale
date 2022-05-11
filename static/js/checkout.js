"use strict"

let page_no = 1

let address_info_elements = document.getElementsByClassName("address-info");
for (let elem of address_info_elements) {
    let parent = elem.parentNode;
    parent.classList.add("address-info-container");
}

let cc_info_elements = document.getElementsByClassName("cc-info");
for (let elem of cc_info_elements) {
    let parent = elem.parentNode;
    parent.classList.add("cc-info-container");
    parent.classList.add("checkout-hidden");
}

function toggleCheckout() {
    for (let elem of address_info_elements) {
            let parent = elem.parentNode;
            parent.classList.toggle("checkout-hidden")
        }
        for (let elem of cc_info_elements) {
            let parent = elem.parentNode;
            parent.classList.toggle("checkout-hidden")
        }
}

function toggleOverview() {
    for (let elem of cc_info_elements) {
            let parent = elem.parentNode;
            parent.classList.toggle("checkout-hidden")
        }
    document.querySelector(".checkout-overview").classList.toggle("checkout-hidden");
    document.querySelector(".checkout-submit-btn").classList.toggle("checkout-visibility-hidden");
}

function updateOverview() {
    let form = document.forms["checkout-form"];
    form["fullname"].setCustomValidity("Hello error");
    form["fullname"].reportValidity()
}

document.querySelector(".checkout-continue-btn").addEventListener('click', function() {
    if (page_no === 1) {
        toggleCheckout()
        document.querySelector(".checkout-back-btn").classList.toggle("checkout-visibility-hidden");
        page_no += 1
    }else if (page_no === 2) {
        updateOverview()
        toggleOverview()
        document.querySelector(".checkout-continue-btn").classList.toggle("checkout-visibility-hidden")
        page_no += 1
    }else if (page_no === 3) {

    }
})

document.querySelector(".checkout-back-btn").addEventListener('click', function() {
    if (page_no === 1) {

    }else if (page_no === 2) {
        toggleCheckout()
        document.querySelector(".checkout-back-btn").classList.toggle("checkout-visibility-hidden");
        page_no -= 1
    }else if (page_no === 3) {
        toggleOverview()
        document.querySelector(".checkout-continue-btn").classList.toggle("checkout-visibility-hidden")
        page_no -= 1
    }
})
/*
let form = document.forms["checkout-form"];
form["fullname"].setCustomValidity("Hello error");
form["fullname"].reportValidity()*/

document.querySelector("#id_credid_card_expiration_date").addEventListener("blur", function(){
    let date_arr = this.value.split("/");
    let month = date_arr[0];
    let year = date_arr[1];
    if (month !== undefined && month !== "" && year !== undefined && year !== "") {
        month = Number(month);
        year = Number(year);
        if (!Number.isNaN(month) && !Number.isNaN(year)) {
            this.setCustomValidity("");
            return;
        }
    }
    this.setCustomValidity("MM/YY")
    this.reportValidity()
})
