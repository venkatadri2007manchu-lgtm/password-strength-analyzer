import secrets
import string

WORDS = ["cipher", "falcon", "shield", "anchor", "matrix", "vector", "orbit", "pulse"]

def generate_suggestions(base_password: str) -> dict:
    passphrase = "-".join(secrets.choice(WORDS) for _ in range(3)) + str(secrets.randbelow(90) + 10)
    charset = string.ascii_letters + string.digits + "!@#$%^&*"
    random_key = "".join(secrets.choice(charset) for _ in range(16))

    return {
        "passphrase": passphrase,
        "random_key": random_key
    }