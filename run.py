from twilio.rest import TwilioRestClient
from flask import Flask, request, render_template
 
twilio_from_number = '6199425133'
twilio_account_sid = 'AC9853752e40599cb7fc11134c166c6866'
twilio_auth_token = '5415da2396c51ffb05d8e84938a9fef1'
 
 
app = Flask(__name__)
client = TwilioRestClient(twilio_account_sid, twilio_auth_token)
 
@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form["name"]
        recipient = request.form["recipient"]
        #call = client.calls.create(to=request.form['phone_number'], 
                           #from_=twilio_from_number, # Must be a valid Twilio number
                           #url=".mp3")
        print "about to send"
        message = client.sms.messages.create(to=request.form['phone_number'], from_= twilio_from_number, body="hi " + recipient + " your friend " +name + " is calling with a special message")
        client.sms.messages.create(
             to=request.form['phone_number'],
             from_=twilio_from_number,
             body='We\'re no strangers to love, You know the rules and so do I, A full commitment\'s what I\'m thinking of, You wouldn\'t get this from any other guy')

        client.sms.messages.create(
             to=request.form['phone_number'],
             from_=twilio_from_number,
             body='http://i288.photobucket.com/albums/ll166/AuraNRGFX/rickroll.gif')

        client.sms.messages.create(
             to=request.form['phone_number'],
             from_=twilio_from_number,
             body='Sent from twilio.  If you want to rickroll your friends, [URL HERE]')
        print "sent"
    return render_template('simple.html')
 
 
if __name__ == "__main__":
    app.run(debug=True)