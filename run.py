from twilio.rest import TwilioRestClient
from flask import Flask, request, render_template

twilio_from_number = '6199425133'

app = Flask(__name__)
client = TwilioRestClient(twilio_account_sid, twilio_auth_token)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        #call = client.calls.create(to=request.form['phone_number'], 
                           #from_=twilio_from_number, # Must be a valid Twilio number
                           #url=".mp3")
        print "about to send"
        message = client.sms.messages.create(to='3012337647', from_='2408216285', body="hi")
        #client.sms.messages.create(to='3012337647',
            #to=request.form['phone_number'],
         #   from_=twilio_from_number,
          #  body='We\'re no strangers to love, You know the rules and so do I, A full commitment\'s what I\'m thinking of, You wouldn\'t get this from any other guy')
        print "sent"
    return render_template('simple.html')


if __name__ == "__main__":
    app.run(debug=True)
