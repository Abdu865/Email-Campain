import sqlite3, base64,io, json, os, time
from flask import Flask, render_template,send_file,request,Response,jsonify
from datetime import datetime


app = Flask(__name__)

@app.route('/')

def index():

 return 'Hello world'

@app.route('/get_my_ip', methods=['GET'])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200


@app.route("/gif", methods=["POST", "GET"])
def gif():
    orign_name = "nowhere"
    address = "nowhere"
    client_ip = ""
    city = ""
    if 'page' in request.args:
        origin_page = request.args.get('page')

        # visitor IP
    client_ip = request.remote_addr 


    pixel_data = base64.b64decode("R0lGODlhAQABAIAAAP8AAP8AACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==")   

    st = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

         # save to file and send thank you note
    with open("pixel-tracker.csv","a") as myfile:
        myfile.write('Timestamp: ' + st + ' client_ip: ' + client_ip + '\n')


    return Response(pixel_data, mimetype="image/gif")

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
