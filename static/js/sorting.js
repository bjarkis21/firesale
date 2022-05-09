"use strict"

function sort_by_title(ads_container) {
    let ads_array = [];
    for (let ad of ads_container) {
        ads_array.push(ad)
    }
    ads_array.sort(function(a,b){
        let title_a = a.querySelector(".ad-title1").textContent.toLowerCase();
        let title_b = b.querySelector(".ad-title1").textContent.toLowerCase();
        if (title_a < title_b){
            return -1
        }else if (title_a > title_b){
            return 1
        }else {
            return 0
        }
    })
    return ads_array
}

function sort_by_date(ads_container) {
    let ads_array = [];
    for (let ad of ads_container) {
        ads_array.push(ad)
    }
    ads_array.sort(function(a,b){
        let time_a = a.querySelector(".ad-creation-date").dataset.timestamp;
        time_a = Number(time_a)
        time_a = new Date(time_a)
        let time_b = b.querySelector(".ad-creation-date").dataset.timestamp;
        time_b = Number(time_b)
        time_b = new Date(time_b)
        if (time_a < time_b){
            return -1
        }else if (time_a > time_b){
            return 1
        }else {
            return 0
        }
    })
    return ads_array
}

document.querySelector("#sort_by_name_asc").addEventListener('click', function(){
    let ads_container = document.getElementsByClassName('ad-anchor1');
    let ads_array = sort_by_title(ads_container)
    let ads_container_element = document.querySelector(".ads-container")
    ads_container_element.innerHTML = ""
    for (let ad of ads_array) {
        ads_container_element.appendChild(ad)
    }
})

document.querySelector("#sort_by_name_desc").addEventListener('click', function(){
    let ads_container = document.getElementsByClassName('ad-anchor1');
    let ads_array = sort_by_title(ads_container).reverse()
    let ads_container_element = document.querySelector(".ads-container")
    ads_container_element.innerHTML = ""
    for (let ad of ads_array) {
        ads_container_element.appendChild(ad)
    }
})

document.querySelector("#sort_by_date_asc").addEventListener('click', function(){
    let ads_container = document.getElementsByClassName('ad-anchor1');
    let ads_array = sort_by_date(ads_container)
    let ads_container_element = document.querySelector(".ads-container")
    ads_container_element.innerHTML = ""
    for (let ad of ads_array) {
        ads_container_element.appendChild(ad)
    }
    console.log("hello")

})

document.querySelector("#sort_by_date_desc").addEventListener('click', function(){
    let ads_container = document.getElementsByClassName('ad-anchor1');
    let ads_array = sort_by_date(ads_container).reverse()
    let ads_container_element = document.querySelector(".ads-container")
    ads_container_element.innerHTML = ""
    for (let ad of ads_array) {
        ads_container_element.appendChild(ad)
    }
    console.log("hello")

})

