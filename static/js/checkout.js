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

document.querySelector(".checkout-continue-btn").addEventListener('click', function() {
    if (page_no === 1) {
        toggleCheckout()
        document.querySelector(".checkout-back-btn").classList.toggle("checkout-visibility-hidden");
        page_no += 1
    }else if (page_no === 2) {

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

    }
})