import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from secret import secret_keys


def send_email_birhtdays():

    msg = MIMEMultipart("related")
    msg["Subject"] = "TESTE: Envio de email com a imagem do aniversariantes"
    msg["From"] = secret_keys.EMAIL_SENDER
    msg["To"] = ", ".join(secret_keys.EMAIL_RECIPIENT)

    with open("email_birthdays/index.html", "r") as file_html:

        html = file_html.read()
        part2 = MIMEText(html, "html", "UTF-8")
        msg.attach(part2)

    with open("images/img_aniversariantes.png", "rb") as file_image:

        image_open = file_image.read()

        msg_image = MIMEImage(image_open)
        msg_image.add_header("Content-ID", "<image1>")
        msg.attach(msg_image)

        image_attach = MIMEImage(image_open, "png")

    msg.attach(image_attach)

    with smtplib.SMTP("smtp.ulh.cloud", port=25) as connection:

        connection.ehlo()
        connection.starttls()
        connection.ehlo()

        connection.send_message(msg)
