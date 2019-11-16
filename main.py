from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, Response, request
from flask_httpauth import HTTPBasicAuth
from camera import VideoCamera
from sys import stdin
import json


app = Flask("main")
auth = HTTPBasicAuth()
cfg = json.load(open('client_config.json'))
users = {
    "user": generate_password_hash("Simple_pass")
}
parent_pid = 0
isauth = bool(cfg['settings']['user_settings']['use_auth'])


@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/')
# @auth.login_required
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/sh")
@auth.login_required
def sh():
    if int(request.args.get('pid')) == parent_pid:
        print("[+] Got stop signal\n[+] Stopping")
        request.environ.get('werkzeug.server.shutdown')()
        return ''


parent_pid = int(stdin.read())
print("[+] parent pid: " + str(parent_pid))
app.run(host='0.0.0.0', port=9000)
