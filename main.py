import json
import boto3
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from problem import generate_problems
from jinja2 import Environment, FileSystemLoader

def main(*args):
    # generate problems and html
    problems = generate_problems(5, ['+', '-'])
    env = Environment(
        loader=FileSystemLoader('./templates'),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template_txt = env.get_template('template.txt')
    template_html = env.get_template('template.html')

    output_txt = template_txt.render(problems=problems)
    output_html = template_html.render(problems=problems)
    # with open('out/out.txt', 'w') as f:
    #     f.write(output_txt)
    # with open('out/out.html', 'w') as f:
    #     f.write(output_html)

    # generate email
    sender = os.environ['MMD_SENDER']
    recipient = os.environ['MMD_RECIPIENT']
    subject = f"Mental Math Drill - {datetime.today().strftime('%m/%d')}"

    message = MIMEMultipart('alternative')
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject

    message.attach(MIMEText(output_txt, 'plain'))
    message.attach(MIMEText(output_html, 'html'))

    # send email
    ses = boto3.client('sesv2')
    response = ses.send_email(
        Content={
            'Raw': {
                'Data': message.as_bytes()
            }
        }
    )

    print(response)

    return {
        'statusCode': 200,
        'body': json.dumps(f"Email sent successfully. MessageId is: {response['MessageId']}")
    }

if __name__ == '__main__':
    response = main()
    print(response)