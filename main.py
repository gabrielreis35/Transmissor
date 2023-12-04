from vidstream import CameraClient
import threading
import time

sending = CameraClient('192.168.15.2', 8000)

th = threading.Thread(target=sending.start_stream)
th.start()

while input("") != "stop":
    continue

sending.stop_stream()
