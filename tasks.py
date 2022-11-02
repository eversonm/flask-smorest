import os
import requests
import jinja2
from dotenv import load_dotenv

load_dotenv()
domain = os.getenv("MAILGUN_DOMAIN")
api_key = os.getenv("MAILGUN_API_KEY")
template_loader = jinja2.FileSystemLoader("templates")
template_env = jinja2.Environment(loader=template_loader)


def render_template(template_filename, **context):
    return template_env.get_template(template_filename).render(**context)


def send_simple_message(to, subject, body, html):

    return requests.post(
        f"https://api.mailgun.net/v3/{domain}/messages",
        auth=("api", api_key),
        data={
            "from": f"Emails with Mailgun <mailgun@{domain}>",
            "to": [to],
            "subject": subject,
            "text": body,
            "html": html
        }
    )


def send_user_registration_email(email):
    username = email.split("@")[0]
    return send_simple_message(
        email,
        "Successfully signed up!",
        f"Hi {username}! You have successfully signed up.",
        render_template("email/action.html", username=username)
    )
