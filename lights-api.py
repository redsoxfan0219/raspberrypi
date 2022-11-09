import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request

# Initialize API

app = Flask(__name__)

# Set up GPIO 

lights_pin = 6
GPIO.setmode(GPIO.BOARD)
GPIO.setup(6, GPIO.OUT)

# Set up decorators

@app.route("/")
def index():
    return render_template('lights.html')
@app.route("/<deviceName>/")
def action(deviceName):
    if deviceName == 'lights':
        relay = lights
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(relay, GPIO.OUT)
        GPIO.output(relay, GPIO.LOW)
        time.sleep(5)
        GPIO.output(relay, GPIO.HIGH)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
