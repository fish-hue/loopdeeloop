import subprocess
import platform
import socket

# Function to ping a range of IPs
def ping_sweep(start_ip, end_ip):
    # Check the current operating system
    ping_option = '-c' if platform.system() != 'Windows' else '-n'
    
    # Convert IPs to integers to handle custom ranges (only for IPs, not domain names)
    if is_ip(start_ip) and is_ip(end_ip):
        start_parts = start_ip.split('.')
        end_parts = end_ip.split('.')
        
        start_ip_int = (int(start_parts[0]) << 24) + (int(start_parts[1]) << 16) + (int(start_parts[2]) << 8) + int(start_parts[3])
        end_ip_int = (int(end_parts[0]) << 24) + (int(end_parts[1]) << 16) + (int(end_parts[2]) << 8) + int(end_parts[3])

        for ip_int in range(start_ip_int, end_ip_int + 1):
            ip = '.'.join(str((ip_int >> (24 - (8 * i))) & 0xFF) for i in range(4))
            res = subprocess.call(['ping', ping_option, '2', ip])
            if res == 0:
                print(f"ITS ALIVE! {ip}")
            elif res != 0:
                print(f"NOBODY WILL ANSWER THE DOOR! :( {ip}")
            else:
                print(f"ping to {ip} failed")
    else:
        # Handle domain names or single IPs
        res = subprocess.call(['ping', ping_option, '2', start_ip])
        if res == 0:
            print(f"ITS ALIVE! {start_ip}")
        elif res != 0:
            print(f"NOBODY WILL ANSWER THE DOOR! :( {start_ip}")
        else:
            print(f"ping to {start_ip} failed")

# Check if the input is a valid IP address
def is_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

# Get user input for the IP range or domain
start_ip = input("Enter the start IP address or domain (e.g., 192.168.1.100 or google.com): ")
end_ip = input("Enter the end IP address (only for IP ranges, or leave blank for single address): ")

# Run the ping sweep for the given IP range or domain
if not end_ip:  # If no end IP is provided, just ping the single start IP or domain
    ping_sweep(start_ip, start_ip)
else:
    ping_sweep(start_ip, end_ip)

