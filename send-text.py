from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token
account_sid = ""
auth_token = ""
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    body = "This is a sample text.",
    to = "",     # Replace with your phone number
    from_ = "")  # Replace with your Twilio number
print message.sid
