import openai
import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

# Set up OpenAI API credentials
app = Flask(__name__)
API_KEY = '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'
openai.api_key = API_KEY
model_engine = "text-davinci-003"
account_sid = 'AC00b18863b13dac39fdf5d91c1bf4a38e'
auth_token = '10ed2a2f13c18d09b3fded8f125fa9a5'
client = Client(account_sid, auth_token)

def generate_answer(question):
    # Get the message from the user
    
    #print(msg)
    # Send the message to ChatGPT for generating a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=question,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    print(completion.get("choices")[0]['text'])
   
    return(completion.get("choices")[0]['text'])

   # generated_text = response.get("choices")[0]['text']
@app.route("/whatsapp", methods=['POST'])
def wa_reply():
    query = request.form.get('Body').lower()
    #sender_number = request.form['From']
    sender_number = request.values.get('From')
    #sender_numberr = ('whatsapp:',sender_number)
    print("User NUMBER:",sender_number)
    print("User Query:",query)
    #question = query
    answer = generate_answer(query)
    
    twilio_response = MessagingResponse()
    reply = twilio_response.message()
    reply.body(answer)
    
    client.messages.create(
        from_='whatsapp:+14155238886',
        body=answer,
        to=sender_number#'whatsapp:{}'.format(sender_number)
    )
    
    return str(twilio_response)


    print(message.sid)
    return str(twilio_response)
    ##print(generated_text)
    # Send the generated response back to the user
    #resp = MessagingResponse()
    #resp.message(generated_text)
    #return str(resp)

#if __name__ == "__main__":
 ##   app.run(debug=True)
#python -m flask run
    #ngrok http 5000
    
