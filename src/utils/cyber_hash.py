from hashlib import sha512
from .app_config import AppConfig

class CyberHash:
    @staticmethod
    def hash(text):
        encode_text = text.encode("utf-8") + AppConfig.password_salt.encode("utf-8")
        hashed_text = sha512(encode_text).hexdigest()
        # output_text = hashed_text.hexdigest()  ## potential if i will need the object in hashed_text - the return output is the same as above
        return hashed_text