import random
import string


def generate_random_user():
    def random_string(length=8):
        return ''.join(random.choices(string.ascii_lowercase, k=length))
    return {
        "email": f"{random_string(8)}@test.com",
        "password": random_string(8),
        "name": random_string(6)
    }

