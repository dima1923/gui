class user(object):
    def __init__(self,login,password):
        self.login=login
        self.password=password
    def admin_or_user(self):
        for i in USERS:
            if(self.password==i.password and self.login==i.login):
                return "USER"
        for i in ADMIN:
            if(self.login==i.login and self.password==i.password):
                return "ADMIN"

USERS = [user('qwe@mail.ru', '1234'), user('ewq@yandex.ru','4321')]
ADMIN = [user('rty@google.com','1234'), user('poi@ya.ru','0000')]
