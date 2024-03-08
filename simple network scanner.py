# bulding a simple network scanner 
#Step 1: Import necessary libraries(make sure you have Scapy installed)
import sys
import scapy
from scapy.all import ARP, Ether, srp
import socket

#step 2: Define the fuction to the scan
def scan_network(ip_range):
    devices = [] #intilize the device list
    arp = ARP(pdst=ip_range)
    ether = Ether(dst = "ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=False)[0]
    for sent, received in result:
        devices.append({'ip':received.psrc, 'mac':received.hwsrc})
    return devices
#step 3: Get IP range from user
def get_ip_range():
    ip_range = input ("enter the ip range to be scanned e.g 192.168.1.0/24")
    return ip_range
#step 4: Display results
def display_results(devices):
    print("IP Addrewss\t\tMAC Address")
    print("_______________________")
    for device in devices:
        print(f"{device['ip']}\t\t{device['mac']}")
# putting it all together
def main():
    ip_range = get_ip_range
    devices = scan_network(ip_range)
if __name__== "__main__":
    main()
















