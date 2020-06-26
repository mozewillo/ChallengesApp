
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
});