
def send_email(message, recipient, sender="university.help@gmail.com"):
    if "@" not in recipient or "@" not in sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    if not recipient.endswith(('.com', '.ru', '.net')) or not sender.endswith(('.com', '.ru','.net')):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return

    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    if  sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
        return

send_email('Это сообщение для проверки связи', 'lada.tranevskaya@mail.ru')
send_email('Вы видите это сообщение как лучший студент курса!', 'lada.tranevskaya@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'lada.tranevskaya@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'lada.tranevskaya@mail.ru', sender='lada.tranevskaya@mail.ru')

