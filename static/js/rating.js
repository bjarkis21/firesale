$("star-rating").click(function() {
    $(this).css({"color" : "orange"});
    $(this).nextAll().css({"color" : "orange"});
});