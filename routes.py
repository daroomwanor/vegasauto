import os
from twilio.rest import Client
from os import environ
from flask import Flask
from flask import render_template, request
import json
import requests
from datetime import datetime
import calendar
import datetime


account_sid = "ACe38cfe0f37370c46431195646cb0833d"
auth_token = "d2297100953b1d5a4ec49c3dba1ddda4"
client = Client(account_sid, auth_token)
app=Flask(__name__)

@app.route("/send_sms", methods=['GET', 'POST'])
def send_sms():
    data = json.loads(request.data)
    print(data)
    message = client.messages.create(
        body= data['message'],
        from_='+17028196491',
        to=data['phone']
    )
    return message.sid

@app.route("/sms_form", methods=['GET', 'POST'])
def index():
    return render_template("send_sms.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0")
