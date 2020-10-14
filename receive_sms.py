from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from credentials import account_sid, auth_token, my_cell, my_twillio,name_my_cell

app = Flask(__name__)

@app.route("/sms",methods=['GET','POST'])
def sms_reply():
    resp = MessagingResponse()

    resp.message("The robots are coming! ")

    return str(resp)

if __name__ =="__main__":
    app.run(debug=True)
