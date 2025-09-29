from flask import Flask, render_template, request
from cryptography.fernet import Fernet
from Crypto.Cipher import AES
import base64
import os

app = Flask(__name__)

# Generate key for Fernet
fernet_key = Fernet.generate_key()
fernet = Fernet(fernet_key)

#  Routes  #

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


#  Encryption/Decryption #

def encrypt_aes(plain_text, key):
    # Generate random 16 bytes IV
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    encrypted_bytes = cipher.encrypt(plain_text.encode())
    return base64.urlsafe_b64encode(iv + encrypted_bytes).decode()

def decrypt_aes(encrypted_text, key):
    raw = base64.urlsafe_b64decode(encrypted_text)
    iv = raw[:16]
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    decrypted_bytes = cipher.decrypt(raw[16:])
    return decrypted_bytes.decode()


@app.route("/process", methods=["POST"])
def process():
    text = request.form["text"]
    action = request.form["action"]
    method = request.form["method"]

    result = ""

    if method == "fernet":
        if action == "encrypt":
            result = fernet.encrypt(text.encode()).decode()
        else:
            try:
                result = fernet.decrypt(text.encode()).decode()
            except Exception:
                result = "❌ Invalid Fernet Token"

    elif method == "aes":
        # AES key 32 bytes
        aes_key = b"This_is_a_secret_key_123456789012"  # Fixed length 32
        if action == "encrypt":
            result = encrypt_aes(text, aes_key)
        else:
            try:
                result = decrypt_aes(text, aes_key)
            except Exception:
                result = "❌ Invalid AES Data"

    return render_template("index.html", result=result)


# ---------------- Run ---------------- #
if __name__ == "__main__":
    app.run(debug=True)
