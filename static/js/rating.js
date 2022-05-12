$("star-rating").click(function() {
    $(this).parent().find("star-rating").css({"color" : "black"});
    $(this).css({"color" : "orange"});
    $(this).nextAll().css({"color" : "orange"});
});