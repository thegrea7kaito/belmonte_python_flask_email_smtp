from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'garybelmonte16@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'kkkg eyzg opur masc'  # Replace with your email password

mail = Mail(app)

# POST /send-email: Send an email
@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    email = data.get('email')
    message_body = data.get('message')

    if not email or not message_body:
        return jsonify({"message": "Email and message are required"}), 400

    try:
        msg = Message(
            "A Message From Flask SMTP App", 
            sender=app.config['MAIL_USERNAME'],
            recipients=[email]
        )
        msg.body = message_body
        mail.send(msg)
        return jsonify({"message": "Email sent successfully"}), 200
    except Exception as e:
        return jsonify({"message": "Failed to send email", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
