from flask import Flask, render_template


app = Flask("mainSRV")
streamers = ['http://10.90.130.37:9000/', 'http://10.90.131.105:9000/', 'http://10.90.130.34:9000/', 'http://10.90.130.204:9000/']


@app.route('/')
def video_feed():
    return render_template("site.html", CAM01=streamers[0], CAM02=streamers[1], CAM03=streamers[2], CAM04=streamers[3])


app.run(host='0.0.0.0', debug=1, port=9001)
