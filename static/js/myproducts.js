"use strict"

let ad_btns = document.getElementsByClassName('deactivate-btn')

for (let ad_btn of ad_btns) {
    ad_btn.addEventListener('click', function(e){
        const ad_id = this.value
        axios.get('http://localhost:8000').then(function(res){console.log(res)})
    })
}