from twilio.rest import TwilioRestClient
from flask import Flask, request, render_template
import time
 
twilio_from_number = '6199425133'
# put in your account sid and token
twilio_account_sid = 'AC9853752e40599cb7fc11134c166c6866'
twilio_auth_token = '5415da2396c51ffb05d8e84938a9fef1'
 
 
app = Flask(__name__)
client = TwilioRestClient(twilio_account_sid, twilio_auth_token)
 
@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form["name"]
        recipient = request.form["recipient"]
        print "about to send"
        
        message = client.sms.messages.create(to=request.form['phone_number'], from_= twilio_from_number, body="Hi " + recipient + " your friend " +name + " is calling with a special message")        
        
        time.sleep(1)

        client.sms.messages.create(
             to=request.form['phone_number'],
             from_=twilio_from_number,
             body='http://images.wikia.com/dragonball/images/f/f3/Rick_astley.gif')

        call = client.calls.create(url="http://demo.twilio.com/docs/voice.xml",
            to= request.form['phone_number'],
            from_="6199425133")

        time.sleep(1)

        client.sms.messages.create(
             to=request.form['phone_number'],
             from_=twilio_from_number,
             body='We\'re no strangers to love, You know the rules and so do I, A full commitment\'s what I\'m thinking of, You wouldn\'t get this from any other guy')

        time.sleep(1)

        client.sms.messages.create(
             to=request.form['phone_number'],
             from_=twilio_from_number,
             body='I just wanna tell you how I\'m feelin. Gotta make you understand. ')

        time.sleep(1)

        client.sms.messages.create(
             to=request.form['phone_number'],
             from_=twilio_from_number,
             body='Never gonna give you up. Never gonna let you down. Never gonna run around and desert you. ')

        time.sleep(1)

        client.sms.messages.create(
             to=request.form['phone_number'],
             from_=twilio_from_number,
             body='Never gonna make you cry. Never gonna say goodbye. Never going to tell a lie, and hurt you.')

        time.sleep(1)

        client.sms.messages.create(
             to=request.form['phone_number'],
             from_=twilio_from_number,
             body='Sent with love, using Twilio.  If you want to rickroll your friends, visit http://sallysapp.herokuapp.com/')
        print "sent"
    return render_template('simple.html')
 
 
if __name__ == "__main__":
    app.run(debug=True)