import sys
import time
import socket
sys.path.append("../")


from dfrobot_huskylensv2 import *

# =====================
# NETWORK SETTINGS
# =====================

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

HOST = "0.0.0.0"
PORT = 5000

print(f"Listening on port {PORT}")

HOST = "0.0.0.0"
PORT = 5000

# =====================
# HUSKYLENS SETUP
# =====================

huskylens = HuskylensV2_I2C()

print("Knock:", huskylens.knock())
print("Switch:", huskylens.switchAlgorithm(ALGORITHM_HAND_RECOGNITION))

# =====================
# MAIN LOOP
# =====================

last_id = None

try:

    while True:

        count = huskylens.getResult(ALGORITHM_HAND_RECOGNITION)

        if count and huskylens.available(ALGORITHM_HAND_RECOGNITION):

            result = huskylens.getCachedResultByIndex(ALGORITHM_HAND_RECOGNITION,
                0
            )

            if result:

                gesture_id = result.ID
                gesture_name = result.name

                if gesture_id != last_id:

                    print(
                        f"Gesture: {gesture_id} "
                        f"({gesture_name})"
                    )

                    if gesture_id == 2:
                        command = "FORWARD"

                    elif gesture_id == 3:
                        command = "REVERSE"

                    elif gesture_id == 4:
                        command = "LEFT"

                    elif gesture_id == 5:
                        command = "RIGHT"

                    else:
                        command = "STOP"

                    print("Sending:", command)

                    sock.sendall(
                        (command + "\n").encode()
                    )

                    last_id = gesture_id

        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:

    try:
        sock.sendall(b"STOP\n")
    except:
        pass

    sock.close()

    print("Disconnected")
