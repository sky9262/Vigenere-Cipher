from flask import Flask, render_template, request, jsonify
from JP_Vigenère_Cipher import vigenere_decrypt as JP_decrypt, vigenere_encrypt as JP_encrypt
from EN_Vigenère_Cipher import vigenere_decrypt as EN_decrypt, vigenere_encrypt as EN_encrypt



app = Flask(__name__, static_url_path='/static', static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encryption():
    plain_text = request.form['plaintext']
    key = request.form['key']
    isEnglish = request.form['isEnglish']
    if isEnglish == "true":
        result = EN_encrypt(plain_text, key)
    else:
        result =  JP_encrypt(plain_text, key)
    # print(result)
    return jsonify(result=result)


@app.route('/decrypt', methods=['POST'])
def decryption():
    encrypted_text = request.form['encryptedText']
    key = request.form['key']
    isEnglish = request.form['isEnglish']
    if isEnglish == "true":
        result = EN_decrypt(encrypted_text, key)
    else:
        result =  JP_decrypt(encrypted_text, key)
    # print(result)
    return jsonify(result=result)


@app.route('/encrypt', methods=['GET'])
def encrypt_get():
    language = request.args.get('lan')
    text = request.args.get('txt')
    key = request.args.get('key')
    type = request.args.get('type')
    if language == "eng":
        result = EN_encrypt(text, key)
    elif language == "jap":
        result = JP_encrypt(text, key)
    else:
        result = "Language not supported"
    if type == "json":
        return jsonify(result=result)
    else:
        return result


@app.route('/decrypt', methods=['GET'])
def decrypt_get():
    language = request.args.get('lan')
    text = request.args.get('txt')
    key = request.args.get('key')
    type = request.args.get('type')
    if language == "eng":
        result = EN_decrypt(text, key)
    elif language == "jap":
        result = JP_decrypt(text, key)
    else:
        result = "language not supported"
    if type == "json":
        return jsonify(result=result)
    else:
        return result


if __name__ == '__main__':
    app.run(debug=True)
