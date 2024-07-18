import boto3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from problem import generate_problems
from jinja2 import Environment, FileSystemLoader

# generate problems and html
problems = generate_problems(5, ['+', '-'])
env = Environment(loader=FileSystemLoader('./templates'))
template = env.get_template('template.html')

output = template.render(problems=problems)
with open('out/out.html', 'w') as f:
    f.write(output)

# generate email
sender = 'Mental Math Drill <no-reply@kpdata.dev>'
recipient = 'Kishan <kishanpatel789@gmail.com>'
subject = f"Mental Math Drill - {datetime.today().strftime('%m/%d')}"

message = MIMEMultipart('alternative')
message['From'] = sender
message['To'] = recipient
message['Subject'] = subject

body_text = 'This is a test message.'
body_html = output

message.attach(MIMEText(body_text, 'plain'))
message.attach(MIMEText(body_html, 'html'))

# send email
ses = boto3.client('sesv2')
ses.send_email(
    Content={
        'Raw': {
            'Data': message.as_bytes()
        }
    }
)