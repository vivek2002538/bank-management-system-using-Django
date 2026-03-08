import hashlib

def hide(pin):
    hidden=hashlib.sha512(str(pin).encode()).hexdigest()
    return hidden