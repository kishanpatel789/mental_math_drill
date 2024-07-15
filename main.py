import boto3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

sender = 'Mental Math Drill <no-reply@kpdata.dev>'
recipient = 'Kishan <kishanpatel789@gmail.com>'
subject = f"Mental Math Drill - {datetime.today().strftime('%m/%d')}"

message = MIMEMultipart('alternative')
message['From'] = sender
message['To'] = recipient
message['Subject'] = subject

body_text = 'This is a test message.'
body_html = """
    <html>
    <head>
        <style>
            .problem {
                font-family: 'Courier New', Courier, monospace;
                text-align: right;
                margin: 20px auto;
                width: fit-content;
            }
            .number, .operator {
                display: block;
                margin: 0;
                white-space: pre;
            }
            .line {
                border-top: 1px solid #000;
                margin: 5px 0;
            }
        </style>
    </head>
    <body>
        <p>Hello!</p>
        <p>Welcome to another math <strong>challenge</strong>.</p>
        <div class="problem">
            <span class="number">123</span>
            <span class="operator">+   67</span>
            <div class="line"></div>
        </div>
    </body>
</html>
"""

message.attach(MIMEText(body_text, 'plain'))
message.attach(MIMEText(body_html, 'html'))


ses = boto3.client('sesv2')

ses.send_email(
    Content={
        'Raw': {
            'Data': message.as_bytes()
        }
    }
)