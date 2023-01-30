import os
from flask import Flask, render_template, request
from flask_mail import Mail, Message
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
habits = ["Test habit", "Test habit 2", "Test Habit 3"]

# define globaal vars for senders and recipients
SENDER = os.environ.get('ROOFHERO_USERNAME')
RECIPIENTS = os.environ.get('RECIPIENT_EMAIL')

# instanitate information needed to send an email with the form info
app.config['MAIL_SERVER']=os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = os.environ.get('MAIL_PORT')
app.config['MAIL_USERNAME'] = SENDER
app.config['MAIL_PASSWORD'] = os.environ.get('ROOFHERO_PW')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route("/")
def index():
    return render_template("index.html", habits=habits, title="Habit Tracker - Home")


@app.route("/add", methods=["GET", "POST"])
def add_habit():
    if request.method == "POST":

        # store the request from the form in a variable
        form_fill = request.form.get("habit")

        # append the form information to the habits list (temporary data structure filling in for a db)
        habits.append(form_fill)

        # send an email with the information using the imported "Message" object from Flask-mail
        email_message = Message(
            'New lead from RoofHero',
            sender = SENDER,
            recipients = [RECIPIENTS],
        )
        email_message.body = form_fill
        mail.send(email_message)


    return render_template("add_habit.html", title="Habit Tracker - Add Habit")

if __name__ == '__main__':
    app.run(debug=True)
