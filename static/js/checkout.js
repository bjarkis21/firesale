"use strict"

let address_info_elements = document.getElementsByClassName("address-info");
for (let elem of address_info_elements) {
    let parent = elem.parentNode;
    parent.classList.add("address-info-container");
    parent.classList.add("checkout-active")
}

let cc_info_elements = document.getElementsByClassName("cc-info");
for (let elem of cc_info_elements) {
    let parent = elem.parentNode;
    parent.classList.add("cc-info-container");
}