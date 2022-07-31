from passlib.context import CryptContext

CRIPTO = CryptContext(schemes=['bcrypt'], deprecated = 'auto') # bcrypt helps with hashing

def check_password(password:str, hash_password:str)->bool:
    '''
    This function checks if the password informed by the user generates an equal
    hash (when compared to the one registered on the database).
    '''
    return CRIPTO.verify(password,hash_password)

def hash_generator(new_password:str)->str:
    '''
    This function has a new password as input and returns a encrypted hash.
    '''
    return CRIPTO.hash(new_password)