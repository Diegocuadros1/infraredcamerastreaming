import socket
import pickle
import numpy as np
import cv2

HOST = ''  # Listen on all interfaces
PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)

print(f"Listening on port {PORT}...")
conn, addr = sock.accept()
print(f"Connection from {addr}")

try:
    while True:
        # Read the first 4 bytes for the length
        data_len_bytes = conn.recv(4)
        if not data_len_bytes:
            break

        data_len = int.from_bytes(data_len_bytes, 'big')

        # Read the full payload
        data = b''
        while len(data) < data_len:
            packet = conn.recv(data_len - len(data))
            if not packet:
                break
            data += packet

        if not data:
            break

        # Deserialize
        thermal_image = pickle.loads(data)  # shape (24, 32), dtype float64

        # If grayscale, apply colormap for better viewing
        if len(frame.shape) == 2 or frame.shape[2] == 1:
            # Optional: upscale for easier viewing
            frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_NEAREST)
            frame = cv2.applyColorMap(frame, cv2.COLORMAP_INFERNO)
        else:
            # Resize BGR color frame if desired
            frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_LINEAR)

        # Display
        cv2.imshow('Thermal Stream', frame)

        # Exit on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    print("Interrupted.")
finally:
    conn.close()
    sock.close()
    cv2.destroyAllWindows()
