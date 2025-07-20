from app import get_db_connection

def insert_message(sender, receiver, encrypted_message, timestamp, aes_key):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (sender, receiver, message, aes_key, timestamp) VALUES (%s, %s, %s, %s, %s)",
                   (sender, receiver, encrypted_message, aes_key, timestamp))
    conn.commit()
    cursor.close()
    conn.close()


def get_messages_for_user(username):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT sender, message, aes_key, timestamp FROM messages WHERE receiver = %s", (username,))
    messages = cursor.fetchall()
    cursor.close()
    conn.close()
    return messages
