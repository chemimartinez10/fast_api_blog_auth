from passlib.context import CryptContext
pass_cxt = CryptContext(schemes=['bcrypt'])

class Hash:
    @staticmethod
    def bcrypt(pwd:str) -> str:
        return pass_cxt.hash(pwd)
    
    @staticmethod
    def verify(plain_pwd:str, hashed_pwd:str) -> bool:
        return pass_cxt.verify(plain_pwd,hashed_pwd)
