from flask import Flask, request, render_template, redirect, url_for
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
        
        smtp_server = "smtp.mail.ch"
        smtp_port = 465
        username = "gruppezweihsg@mail.ch"
        password = "H4lloGruppeZwei2!"  
        sender_email = username
        recipients = [username, email]

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = ", ".join(recipients)
        msg['Subject'] = "New Contact Us Message from Website"
        body = f"From: {first_name} {second_name} <{email}>\n\n{message}"
        msg.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
                server.login(username, password)
                server.sendmail(sender_email, recipients, msg.as_string())
            return redirect(url_for('index'))
        except Exception as e:
            print(f"An error occurred: {e}")
            return "Failed to send message."

    return render_template('contact_us.html')  # Ensure this HTML file is in the 'templates' folder

@app.route('/')
def index():
    return render_template('index.html')  # Ensure this HTML file is in the 'templates' folder

if __name__ == "__main__":
    app.run(debug=True)
