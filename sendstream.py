import time
import socket
import cv2
import pickle

cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)  # Device ID
if not cap.isOpened():
    raise RuntimeError("TC001 not found")


WIDTH = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
HEIGHT = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"Frame size: {WIDTH}x{HEIGHT}")

# Setup socket connection
HOST = '192.168.86.30'  # Replace with your Mac’s IP
PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
print(f"Connected to {HOST}:{PORT}")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Frame capture failed.")
            continue
        
        frame = cv2.cvtColor(frame, cv2.COLOR_YUV2BGR_YUY2)

        data = pickle.dumps(frame)

        # Send length of the data first
        sock.sendall(len(data).to_bytes(4, 'big'))
        # Send actual data
        sock.sendall(data)

        print("Frame sent.")
        time.sleep(0.5)  # 2 Hz refresh
except KeyboardInterrupt:
    print("Interrupted.")
finally:
    cap.release()
    sock.close()
