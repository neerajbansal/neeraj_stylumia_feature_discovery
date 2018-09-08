function submitClick(e) {
    e.preventDefault();

    var username = $('#exampleInputUsername1').val();
    var password = $('#exampleInputPassword1').val();

    if (!username || !password) {
        alert('Username/ Password required');
        return;
    }

    $.ajax({
        type: "POST",
        url: baseUrl + 'auth',
        data: JSON.stringify({ "username": username, "password": password }),
        contentType: 'application/json',
        success: function (data) {
            console.log(data)
            window.localStorage.setItem('access_token', data.access_token)
            window.localStorage.setItem('name', data.name)
            window.localStorage.setItem('user_id', data.user_id)
            window.location.href = baseUrl + 'dashboard'
        },
        error: function (error) {
            alert('Wrong Username/ Password');
            return;
        }
    });
}