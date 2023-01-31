import os
import yagmail
from dotenv import load_dotenv
import json

load_dotenv()

yag = yagmail.SMTP(
    os.environ.get('EMAIL_USERNAME'),
    os.environ.get('EMAIL_PW'),
)

contents = [
    "This is the body, and here is just text http://somedomain/image.png",
    "You can find an audio file attached.", '/local/path/to/song.mp3'
]

print("recipient email", os.environ.get('RECIPIENT_EMAIL'))

yag.send(
    to=json.loads(os.environ['RECIPIENT_EMAIL']),
    subject='subject', 
    contents=contents
)


print("done")
