from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from crawl_data import TrungTamDayKem_Crawler

# TODO: gửi thông tin về lớp dạy tiếng Anh phù hợp mỗi 1 giờ qua email

SENDER = 'sender_email@gmail.com'
PASSWORD = 'senders_password'
RECEIVER = 'receiver_email@gmail.com'


# setup the parameters of the message
msg = MIMEMultipart()  # create a message
msg['From'] = SENDER
msg['To'] = RECEIVER
msg['Subject'] = "Thông tin các khóa dạy thêm phù hợp"
# get courses information
data = TrungTamDayKem_Crawler()
message = data.find_courses(loc="Thủ Đức", gen="Sinh viên Nam")
# add to the message body
msg.attach(MIMEText(message, 'plain'))

with SMTP('smtp.gmail.com', 587) as sever:
    sever.starttls()
    sever.login(SENDER, PASSWORD)
    sever.send_message(msg)
