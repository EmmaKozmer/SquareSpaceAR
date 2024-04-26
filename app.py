from flask import Flask, request, render_template_string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route("/contact_us", methods=["GET", "POST"])
def contact_us():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        second_name = request.form.get("second_name")
        email = request.form.get("email")
        message = request.form.get("message")
        
        # Define SMTP email server details
        smtp_server = "smtp.mail.ch"
        smtp_port = 465  # Secure SMTP port
        username = "gruppezweihsg@mail.ch"
        password = "H4lloGruppeZwei2!"  
        sender_email = username
        recipients = [username, email]

        # Create a MIMEText object
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = ", ".join(recipients)
        msg['Subject'] = "New Contact Us Message from Website"
        body = f"From: {first_name} {second_name} <{email}>\n\n{message}"
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Connect to the SMTP server and send the email
            with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
                server.login(username, password)
                server.sendmail(sender_email, recipients, msg.as_string())
            return "Your message has been sent. Thank you!"
        except Exception as e:
            print(f"An error occurred: {e}")
            return "Failed to send message."

    # If GET request, render your contact form.
    return render_template_string(open("contact_us.html").read())  # Using render_template_string for simplicity

if __name__ == "__main__":
    app.run(debug=True)
