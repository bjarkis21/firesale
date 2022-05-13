"use strict"

/*
$("star-rating").click(function() {
    // $(this).parent().find("star-rating").css({"color" : "black"});
    $(this).css({"color" : "orange"});
    $(this).nextAll().css({"color" : "orange"});
    console.log($(this))
});

*/

function fillStars(star_container, star_count) {
    let iter_count = 1;
    let star_arr = star_container.getElementsByClassName("fa-star")
    for (let star of star_arr) {
        let star_number = star.dataset.rating;
        star_number = Number(star_number);
        if (star_number <= star_count) {
            star.classList.add('gold');
        } else {
            star.classList.remove('gold');
        }
    }
}

function sendRating(ad_id, star_count, star_container) {
    axios.post('http://localhost:8000/ads/rate_ad', {
        ad_id: ad_id,
        rating: star_count
    }).then((res) => {
        star_container.classList.add('rated')
    })

}

let star_elements = document.getElementsByClassName("dynamic-star");
console.log(star_elements)
for (let star of star_elements) {
    let parent = star.parentNode;
    if (! parent.classList.contains('rated')) {
        star.addEventListener('click', function() {
            let star_rating = star.dataset.rating;
            star_rating = Number(star_rating);
            fillStars(parent, star_rating);
            sendRating(parent.dataset.adid, star_rating, parent);
        })
    } else {
        let star_rating = parent.dataset.rating.replace(",", ".");
        star_rating = Number(star_rating);
        fillStars(parent, star_rating);
    }
}