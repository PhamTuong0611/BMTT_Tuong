from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vignere import VignereCipher

app = Flask(__name__)

caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

#vignere
vignere_cipher = VignereCipher()

@app.route("/api/vignere/encrypt", methods=["POST"])
def vignere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vignere_cipher.vignere_encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/vignere/decrypt", methods=["POST"])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vignere_cipher.vignere_decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

#main
if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)