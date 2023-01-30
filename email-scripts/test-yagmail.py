import os
import yagmail
from dotenv import load_dotenv

load_dotenv()

yag = yagmail.SMTP(
    os.environ.get('ROOFHERO_USERNAME'),
    os.environ.get('ROOFHERO_PW'),
)

contents = [
    "This is the body, and here is just text http://somedomain/image.png",
    "You can find an audio file attached.", '/local/path/to/song.mp3'
]
yag.send('jburdett1993@gmail.com', 'subject', contents)
