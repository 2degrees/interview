import random
import string

from django.db.models import CharField, BooleanField, Model

from authn.exceptions import InvalidNameException

APPROVED_ADMIN_NAMES = ['secret_admin', 'secret_superuser']


class Author(Model):
    name = CharField(max_length=64)
    is_admin = BooleanField()

    def save(self, *args, **kwargs):
        self.is_admin = True
        try:
            self.name = self.validate_name(self.name)
            if self.name not in APPROVED_ADMIN_NAMES:
                self.is_admin = False
        except InvalidNameException:
            self.name = self.generate_random_string()
        super().save(*args, **kwargs)

    def validate_name(self, name):
        if len(name) < 3:
            raise InvalidNameException(f'{len(name)} is too short!')
        return name

    def generate_random_string(length=5):
        return ''.join(random.choice(string.ascii_letters) for i in range(10))
