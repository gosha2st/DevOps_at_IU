from flask import Flask
from datetime import datetime
import os.path
import os
import pytz

LOG_FILENAME = './access.log'

app = Flask(__name__)

# Retrieve Moscow timezone:
tz_Moscow = pytz.timezone("Europe/Moscow")

@app.route('/')
def main_time():
    # Retrieve current time in the specified timezone:
    cur_time = datetime.now(tz_Moscow).strftime("%H:%M:%S")
    # Create LOG file and add the latest entry:
    with open(LOG_FILENAME, 'a') as curfile:
        curfile.write(cur_time + '\n')
    # Render web-app main content:
    return f"<center>Current Moscow time (UTC+03:00): {cur_time}</center>"

# Visits counter:
@app.route('/visits')
def show_visits():
    with open(LOG_FILENAME, 'r') as curfile:
        return '<div>'.join(curfile.readlines())

if __name__ == '__main__':
    app.run()
