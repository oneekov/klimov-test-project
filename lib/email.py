import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


class EmailSender:
    def __init__(self, host, port, username, password, use_ssl=True):
        """
        Инициализирует объект EmailSender для отправки писем через SMTP.

        :param host: Адрес SMTP-сервера (например, 'smtp.gmail.com')
        :param port: Порт SMTP-сервера (например, 465 для SSL, 587 для TLS)
        :param username: Логин (адрес электронной почты)
        :param password: Пароль или App Password
        :param use_ssl: Использовать SSL (True для порта 465, False для TLS на порту 587)
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.use_ssl = use_ssl
        if self.use_ssl:
            self.server = smtplib.SMTP_SSL(self.host, self.port)
        else:
            self.server = smtplib.SMTP(self.host, self.port)
            self.server.starttls()
        self.server.login(self.username, self.password)

    def send(self, to_email, html_content):
        """
        Отправляет HTML-письмо на указанный адрес.

        :param to_email: Адрес получателя
        :param html_content: HTML-содержимое письма
        """
        # Создаем MIME-сообщение
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = to_email
        msg['Subject'] = Header('Спасибо за прохождение теста Климова!', 'utf-8')

        # Добавляем HTML-содержимое
        msg.attach(MIMEText(html_content, 'html', 'utf-8'))

        # Отправка письма
        self.server.sendmail(self.username, to_email, msg.as_string())

class EmailSenderOffline:
    def send(self, to_email, html_content):
        """
        Заглушка для отправки писем в оффлайн-режиме.

        :param to_email: Адрес получателя
        :param html_content: HTML-содержимое письма
        """
        pass
