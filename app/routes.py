from flask import request, jsonify, render_template
from app import app
from app.models import insert_message, get_messages_for_user
from app.crypto_utils import encrypt_message
import os
from datetime import datetime

from base64 import b64encode
from app.crypto_utils import decrypt_message

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/send', methods=['POST'])
def send():
    data = request.json
    sender = data['sender']
    receiver = data['receiver']
    message = data['message']
    aes_key = os.urandom(16)
    encrypted_msg = encrypt_message(message, aes_key)
    aes_key_b64 = b64encode(aes_key).decode()
    insert_message(sender, receiver, encrypted_msg, datetime.now(), aes_key_b64)
    return jsonify({'status': 'success'})

@app.route('/inbox')
def inbox():
    user = request.args.get('user')
    if not user:
        return jsonify({'status': 'error', 'message': 'No user provided'}), 400
    messages = get_messages_for_user(user)
    result = []
    for m in messages:
        decrypted = decrypt_message(m[1], m[2])
        result.append({'from': m[0], 'message': decrypted, 'timestamp': str(m[3])})
    return jsonify(result)