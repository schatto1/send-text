from twilio.rest import Client

# Your Account Sid and Auth Token
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

message = client.messages.create(
    body = "Hellooooo from the other siiiiiiiide",
    to = "",     # Replace with your phone number
    from_ = "")  # Replace with your Twilio number
print(message.sid)
