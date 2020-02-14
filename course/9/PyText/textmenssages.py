from twilio.rest import Client

account_sid = "ACaffd83d56704080ae2c850426a50c413"
auth_token = "6de11d818a0fc9bac9ece4e9b8fcca06"
client = Client(account_sid, auth_token)

call = client.messages.create(
    to="+14073420147",
    from_="+13233195264",
    body="eres una mariquita"
)
