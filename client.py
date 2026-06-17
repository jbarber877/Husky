import socket
import time
import RPi.GPIO as GPIO

# =====================
# MOTOR PINS
# =====================

IN1 = 17
IN2 = 27
IN3 = 22
IN4 = 23

FAN = 21

GPIO.setmode(GPIO.BCM)

for pin in [IN1, IN2, IN3, IN4, FAN]:
    GPIO.setup(pin, GPIO.OUT)

GPIO.output(FAN, 1)

# =====================
# MOTOR FUNCTIONS
# =====================

def stop():
    GPIO.output(IN1, 0)
    GPIO.output(IN2, 0)
    GPIO.output(IN3, 0)
    GPIO.output(IN4, 0)

def forward():
    GPIO.output(IN1, 1)
    GPIO.output(IN2, 0)
    GPIO.output(IN3, 1)
    GPIO.output(IN4, 0)

def reverse():
    GPIO.output(IN1, 0)
    GPIO.output(IN2, 1)
    GPIO.output(IN3, 0)
    GPIO.output(IN4, 1)

def left():
    GPIO.output(IN1, 0)
    GPIO.output(IN2, 1)
    GPIO.output(IN3, 1)
    GPIO.output(IN4, 0)

def right():
    GPIO.output(IN1, 1)
    GPIO.output(IN2, 0)
    GPIO.output(IN3, 0)
    GPIO.output(IN4, 1)

# =====================
# SERVER
# =====================

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

server.bind((HOST, PORT))
server.listen(1)

print("Waiting for connection...")

conn, addr = server.accept()

print("Connected from:", addr)

last_command_time = time.time()

try:

    while True:

        conn.settimeout(0.1)

        try:

            data = conn.recv(1024)

            if data:

                command = (
                    data.decode()
                    .strip()
                    .upper()
                )

                print("Received:", command)

                last_command_time = time.time()

                if command == "FORWARD":
                    forward()

                elif command == "REVERSE":
                    reverse()

                elif command == "LEFT":
                    left()

                elif command == "RIGHT":
                    right()

                elif command == "STOP":
                    stop()

        except socket.timeout:
            pass

        # Safety timeout
        if time.time() - last_command_time > 1.0:
            stop()

except KeyboardInterrupt:
    pass

finally:

    stop()

    GPIO.cleanup()

    conn.close()
    server.close()
