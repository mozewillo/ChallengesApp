
$(document).ready(function() {
    $('.plus-button').click(function () {
        var tr = $(this).parent().parent();
        var pk = tr.find('.id').text();
        $.get('/ajax/increment?id=' + pk, function (data) {
            /* zmiana w wierszu */
            tr.find('.counter-text').text(data);
            tr.find('.counter-edit').val(data);
            tr.find('.progress').text(Math.round(tr.find('.counter-text').text() / tr.find('.days_total-text').text() * 100) + '%');
        });
    });

        $('.ajax-save').click(function() {
        var tr = $(this).parent().parent();
        var csrftoken = getCookie('csrftoken');
        var pk = tr.prop('id');
        var name = tr.find('.name-edit').val();
        var description = tr.find('.description-edit').val();
        var duration = tr.find('duration-edit').val();
        var counter = tr.find('.counter-edit').val();
        var version = tr.attr('version');
        $.post('/ajax/save/',
		  { 'csrfmiddlewaretoken': csrftoken,
		    'id': pk,
		    'name': name,
            'description': description,
            'duration': duration,
            'counter': counter,
            'version': version,
		  },
		function(data) {
             // version control
            if (data == '0') {
                tr.find('.name-text').text(name);
                tr.find('.description-text').text(description);
                tr.find('.duration-text').text(duration);
                tr.find('.counter-text').text(counter);

            }
            if (data == '2') {
                alert('Your edit has not been saved, data was changed during your edit')
            }
        });
    });

        $('.ajax-delete').click(function(){
            var csrftoken = getCookie('csrftoken');
            var tr = $(this).parent().parent();
            var pk = tr.find('.id').text();
            tr.hide()
            $.post('/ajax/delete/',
            { 'csrfmiddlewaretoken': csrftoken,
            'id': pk,
        });
    });

});




// using cookies
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
