import random
import string

class Helpers:

    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def generate_random_email(self, domain='mail.ru', username_prefix='DianaKo1989'):
        random_number = random.randint(0, 9999)
        login = f'{username_prefix}{random_number}'
        email = f'{login}@{domain}'
        return email
    
    def generate_user(self):
        email = self.generate_random_email()
        password = self.generate_random_string(10)
        name = self.generate_random_string(10)
        return email, password, name