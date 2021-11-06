from cryptography.fernet import Fernet


def pri():
    cualquiera = " cualquiera "
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(cualquiera.encode())
    print(token)
    Origin = f.decrypt(token)
    print(Origin.decode())


pri()
