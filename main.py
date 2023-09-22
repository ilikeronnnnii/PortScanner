import socket


def scan(target, selected_ports):
    for port in range(1, int(selected_ports)):
        scan_port(target, port)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Opened " + str(port))
    except:
        print("[-] Port Closed " + str(port))


targets = input("[*] Enter Targets To Scan: ")
ports = input("[*] Enter How Many Ports You Want To Scan: ")

if ',' in targets:
    print("[*] Scanning Multiple Targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets, ports)
