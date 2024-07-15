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
        </head>
        <body>
            <p>Hello!</p>
            <p>Welcome to another math <strong>challenge</strong>.</p>
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