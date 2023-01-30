***Under development

run ```python app.py``` to run app in debug mode locally

You need to create a `.env` file locally at the root of the project and fill out the following:
```
ROOFHERO_USERNAME=''
ROOFHERO_PW=''
MAIL_SERVER=''
MAIL_PORT=''
RECIPIENT_EMAIL=''
```

`email-scripts/test-smtplib.py` is designed to test your email credentials.  Simply execute ```python test-email.py``` from root once your .env is filled out, and you should get an email in your `RECIPIENT_EMAIL` location.

`email-scripts/test-yagmail.py` allows for an easy custom email message.  This convention is adoped in the Flask app.
