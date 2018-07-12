import os
import logging
from flask import jsonify
from flask import Flask
from flask import request
from flask_httpauth import HTTPBasicAuth


AUTH_USERNAME = os.environ['API_USERNAME']
AUTH_PASSWORD = os.environ['API_KEY']


# Setup the app
app = Flask(__name__)
app.debug = False
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    if username == AUTH_USERNAME and password == AUTH_PASSWORD:
        return True
    else:
        return False


@app.route('/v1/test')
@auth.login_required
def get_test():
    args = request.args.get('attr_name', None)
    response = {'status': 'ok', 'auth': True}
    return jsonify(response)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
