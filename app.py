from dotenv import load_dotenv
from flask import Flask, render_template, request
import os
import yagmail
import json

load_dotenv()

app = Flask(__name__)
habits = ["Test habit", "Test habit 2", "Test Habit 3"]


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

        # send an email using yagmail -- first instantiate a yag object with credentials
        yag = yagmail.SMTP(
            os.environ.get('EMAIL_USERNAME'),
            os.environ.get('EMAIL_PW'),
        )

        contents = [
            "This is your first Lead",
            "Here's the contact info:",
            form_fill,
        ]

        yag.send(
            to=json.loads(os.environ['RECIPIENT_EMAIL']),
            subject='Lead',
            contents=contents,
        )


    return render_template("add_habit.html", title="Habit Tracker - Add Habit")

if __name__ == '__main__':
    app.run(debug=True)
