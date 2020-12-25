from flask import Flask, render_template
import serial
ser = serial.Serial()
app = Flask(__name__)
@app.route('/<port>')
def index(port):
    ser.baudrate = 9600
    ser.port = 'COM'+port
    ser.open()
    temperature = ser.readline()
    temperature = temperature.decode()
    temperature = temperature.split(",")
    ser.close()
    return render_template("index.html", temp=temperature[0], hum=temperature[1])

if __name__=='__main__':
    app.run()