import socket
import paramiko
import os
import urllib.request
from datetime import datetime

# Function to show local date and time
def show_date_time():
    """Display the local date and time."""
    print("Local Date and Time:", datetime.now())

# Function to show local machine's IP address
def show_ip_address():
    """Display the IP address of the local computer."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        # Connect to a dummy IP (doesn't matter, just to get local IP)
        s.connect(('10.254.254.254', 1))
        local_ip = s.getsockname()[0]
        s.close()
        print("Local IP Address:", local_ip)
    except Exception as e:
        print("Error retrieving local IP address:", str(e))
