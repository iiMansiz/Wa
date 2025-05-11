from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

# Pastikan Anda telah mengatur variabel lingkungan untuk SID Akun dan Auth Token Twilio Anda
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

# Nomor WhatsApp Twilio Anda (format: whatsapp:+...)
TWILIO_WHATSAPP_NUMBER = os.environ.get("TWILIO_WHATSAPP_NUMBER")

@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    incoming_msg = request.values.get("Body", "").lower()
    sender_number = request.values.get("From")
    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg == "menu":
        msg.body("Hai!")
    else:
        msg.body("Anda mengetik: {}".format(incoming_msg)) # Balas dengan pesan yang diterima

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
