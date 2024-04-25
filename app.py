from flask import Flask, request, render_template_string
import smtplib

app = Flask(__name__)

@app.route("/contact_us", methods=["GET", "POST"])
def contact_us():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        second_name = request.form.get("second_name")
        email = request.form.get("email")
        message = request.form.get("message")
        
        # Your email logic here. Example with smtplib:
        sender = "your@example.com"
        password = "your_password"  # It's better to use environment variables or input for security reasons
        recipients = ["recipient1@example.com", "recipient2@example.com"]
        
        with smtplib.SMTP("smtp.example.com", 587) as server:
            server.starttls()
            server.login(sender, password)
            email_message = f"Subject: New Contact Us Message\n\nFrom: {first_name} {second_name} <{email}>\n\n{message}"
            server.sendmail(sender, recipients, email_message)
        
        return "Your message has been sent. Thank you!"
    
    # If GET request, render your contact form.
    return render_template_string(open("contact_us.html").read())  # Using render_template_string for simplicity

if __name__ == "__main__":
    app.run(debug=True)
