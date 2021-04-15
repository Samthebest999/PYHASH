import hashlib
import time 
def file_hash(filepath):
    global hashed_file
    sha256_hash = hashlib.sha256()
    with open(filepath,"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        hashed_file = sha256_hash.hexdigest()
def text_hash(text):
    global hashed_text
    text = text.encode("utf-8")
    hashed_text = hashlib.sha256(text).hexdigest()
