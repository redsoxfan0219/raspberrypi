import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request

# Initialize API

app = Flask(__name__)

# Set up GPIO 

lights_pin = 6
GPIO.setmode(GPIO.BOARD)
GPIO.setup(6, GPIO.OUT)

