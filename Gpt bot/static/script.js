$(document).ready(function() {
    $('#message-form').on('submit', function(event) {
        event.preventDefault();

        var user_input = $('#user_input').val();

        $.ajax({
            url: '/ask',
            type: 'POST',
            data: { user_input: user_input },
            success: function(response) {
                $('#response').text(response);
            }
        });
        
        // Clear the input field
        $('#user_input').val('');
    });
});
