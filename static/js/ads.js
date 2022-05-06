$(document).ready(function() {
    $('search-btn').on( types: 'click', selector: function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax( url: {
            url: '/ads?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class="well ads">
                                <a href="/ads/${d.id}">
                                    <img class="ad-img" src="${d.image}" />
                                    <h4>${d.name}</h4>
                                    <p>${d.short_description}</p>
                                </a>
                            </div>`
                });
                $('.ads').html(newHtml.join(''))
            },
            error: function(xhr, status, error) {
                // TODO: Show toastr
                console.error(error);
            }
        })
    });
});