import os
from flask import Flask, jsonify, render_template, send_from_directory
from flask_restful import Api
from resources.notification import AddNotification, UserNotifications, DeleteUserNotification
from security import authenticate, identity
from flask_jwt import JWT, jwt_required, JWTError


app = Flask(__name__, static_folder='public')
api = Api(app)
app.secret_key = 'asgcbde7t6t2r67t23r23yugrb23yhgr8723ugr23'
jwt = JWT(app, authenticate, identity)


@jwt.auth_response_handler
def customized_response_handler(access_token, identity):
    print(identity)
    return jsonify({
        'access_token': access_token.decode('utf-8'),
        'user_id': identity.id,
        'name': identity.name
    })


# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists("public/" + path):
        return send_from_directory('public', path)
    else:
        return send_from_directory('public', 'index.html')


@app.route('/')
def bootstrap_stylumia():
    return render_template('index.html')


@app.route('/dashboard')
def user_page():
    return render_template('dashboard.html')


@app.route('/admin')
def admin_page():
    return render_template('admin.html')

@app.route('/version1')
def version1():
    return render_template('version1.html')

@app.route('/version2')
def version2():
    return render_template('version2.html')


# # Rest APIs
api.add_resource(UserNotifications, '/api/notification/<int:id>')
api.add_resource(DeleteUserNotification, '/api/notification/<int:id>')
api.add_resource(AddNotification, '/api/notification')


@app.errorhandler(JWTError)
def auth_error_handler(err):
    return jsonify({'message': 'Un-authorized User'}), 401


if __name__ == '__main__':
    app.run(debug=True)
