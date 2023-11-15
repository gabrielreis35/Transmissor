from vidstream import CameraClient
import threading
import time

sending = CameraClient('ip pra quem recebe')

th = threading.Thread(target=sending.start_stream)
th.start()

while input("") != "stop":
    continue

sending.stop_stream()