import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def send_mail():
    s = "bhaskarrawat258@gmail.com"  
    p = "jcdj tqcq gwxu axir"  
    r = "bhaskarrawat258@gmail.com"

    sub = "Challenge 3 Completed"
    b = """
    Name: Bhaskar Singh Rawat
    Semester: 8
    Branch: Computer Science & Engineering
    Roll Number: 2103330109002
    """

    msg = MIMEMultipart()
    msg['From'] = s
    msg['To'] = r
    msg['Subject'] = sub

    msg.attach(MIMEText(b, 'plain'))

    img_path = "Sample.jpg"

    try:
        with open(img_path, 'rb') as img_file:
            img = MIMEImage(img_file.read(), name=os.path.basename(img_path))
            msg.attach(img)
    except FileNotFoundError:
        print(f"Error: Image file '{img_path}' not found.")

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(s, p)
        server.sendmail(s, r, msg.as_string())
        server.quit()
        print("Email with image sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_mail()
