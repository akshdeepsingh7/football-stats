import os
from cryptography.fernet import Fernet

def decrypt_file(enc_file_path, dec_file_path, key):
    with open(enc_file_path, "rb") as f:
        encrypted_data = f.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(dec_file_path, "wb") as f:
        f.write(decrypted_data)

enc_file_path = "main.py.enc"
dec_file_path = "main.py"
key = os.environ["PASSWORD"].encode()

decrypt_file(enc_file_path, dec_file_path, key)
os.system("python main.py")
os.remove("main.py")