"use strict"

document.querySelector("#sort_by_name_asc").addEventListener('click', function(){
    let ads_container = document.getElementsByClassName('ad-anchor1')
    let ads_array = []
    for (let ad of ads_container) {
        ads_array.push(ad)
    }
    console.log(ads_array)
})

