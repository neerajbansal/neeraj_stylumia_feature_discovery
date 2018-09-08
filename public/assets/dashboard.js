if (isLoggedIn()) {
    var notifications = {};

    var getNotifications = new Promise((resolve, reject) => {
        var userId = window.localStorage.getItem('user_id')
        ajaxWrapper('GET', 'api/notification/' + userId, null, function (err, data) {
            console.log(err, data)
            if (err) {
                alert('Your session is expired, please login to continue...');
                reject();
            }
            else {
                notifications = data.notifications;
                resolve('Notifications fetching done');
            }
        })
    })

    getNotifications.then(() => {
        hideLoader();
        renderNotifications(notifications);
    }).catch((err) => {
        alert('No Notifications found');
        hideLoader();
        clearLocalStorage();
    });


    $(document).ready(function () {
        var name = window.localStorage.getItem('name');
        var userId = window.localStorage.getItem('user_id');
        $('#nameSpan span').html("Hi " + name + ", UserId " + userId);
    });

    function renderNotifications(notificationObj) {
        $('#notificationTable').empty();
        // if(!Object.keys(notificationObj).length){
        //     $('#notificationTable').html('No Notificatins Found');
        //     return;
        // }
        for (var item in notificationObj) {
            var bars = '';
            bars += '<div class="col-md-12 alert alert-success">'
            bars += '<span>' + notificationObj[item]['msg'] + '</span>';

            bars += '<button type="button" onclick="deleteNotification(' + notificationObj[item]['id'] + ')" class="btn btn-link btn-danger">Delete</button>';

            bars += '<button type="button" onclick="RedirectTo(' + "'"+ notificationObj[item]['see_more_handler'] + "'" + ')" target="_blank" class="btn btn-link btn-danger">Know More</button>';
            bars += '</div>';
            $('#notificationTable').append(bars);

        }
    }

    var RedirectTo = function(url){
        window.location.href = baseUrl + url;
        console.log(url);
    }

    var deleteNotification = function (id) {
        var url = 'api/notification/' + id;
        showLoader();
        ajaxWrapper('DELETE', url, null, function (err, data) {
            hideLoader();
            if (err) {
                alert(err.responseJSON.message);
            }
            else {
                alert(data.message);
                notifications = notifications.filter((user) => { return user.id != id });
                renderNotifications(notifications);
            }
        })
    }

}

