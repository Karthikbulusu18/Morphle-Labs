from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz
import pwd

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Name - your full name
    full_name = "Karthik Bulusu"  # Replace with your actual full name

    # Username - system username
    try:
        username = pwd.getpwuid(os.getuid()).pw_name
    except Exception:
        username = "Unknown"

    # Server Time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Top output
    try:
        top_output = subprocess.getoutput('top -b -n 1')
    except Exception as e:
        top_output = str(e)

    # Prepare HTML output
    html = f"""
    <h1>/htop Endpoint</h1>
    <p><strong>Name:</strong> {full_name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz
import pwd

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Name - your full name
    full_name = "Karthik Bulusu"  # Replace with your actual full name

    # Username - system username
    try:
        username = pwd.getpwuid(os.getuid()).pw_name
    except Exception:
        username = "Unknown"

    # Server Time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Top output
    try:
        top_output = subprocess.getoutput('top -b -n 1')
    except Exception as e:
        top_output = str(e)

    # Prepare HTML output
    html = f"""
    <h1>/htop Endpoint</h1>
    <p><strong>Name:</strong> {full_name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
