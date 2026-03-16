from passlib.context import CryptContext

hash_context = CryptContext(schemes=['argon2'],deprecated="auto")


def hash_password(password):
    hashed = hash_context.hash(password)
    return hashed



def verify(hashed,password):
    v = hash_context.verify(password,hashed)