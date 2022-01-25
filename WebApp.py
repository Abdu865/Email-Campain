import base64,os ,time
from flask import Flask,request,Response, redirect, url_for
from datetime import datetime


app = Flask(__name__)

@app.route('/',host="hijazz.solutions")

def index():

 return 'Hello world'



@app.route("/gif", methods=["POST", "GET"])
def gif():
    client_ip = ""
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
