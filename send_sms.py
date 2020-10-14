from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twillio,name_my_cell

client = Client(account_sid,auth_token)

for i in range(len(name_my_cell)):
    text = '''{} \nSay hi back to me, testing, testing...1....2...3...?'''
    my_msg = text.format(name_my_cell[i])

    message = client.messages.create(to=my_cell[i],from_=my_twillio,
                                     body=my_msg)
