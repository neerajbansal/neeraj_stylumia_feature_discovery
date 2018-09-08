function submitNotification(e) {
    e.preventDefault();

    var user_id = $('#user_id').val();
    var msg = $('#msg').val();

    if (!user_id || !msg) {
        alert('UserId/ Message required');
        return;
    }

    $.ajax({
        type: "POST",
        url: baseUrl + 'api/notification',
        data: JSON.stringify({ "user_id": user_id, "msg": msg }),
        contentType: 'application/json',
        success: function (data) {
            alert(data.message);
            return;
        },
        error: function (error) {
            alert('No Such User Exist!')
            // alert(error.message);
            return;
        }
    });
}