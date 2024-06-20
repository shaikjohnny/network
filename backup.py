from netmiko import ConnectHandler
from datetime import datetime
import os

# Define the device details
cisco_device = {
    'device_type': 'cisco_ios',
    'host': '10.100.96.81',  # Replace with your router's IP address
    'username': 'cisco',  # Replace with your router's username
    'password': 'ffappcc@aa',  # Replace with your router's password
    #'secret': 'secret',  # Enable password if required
}

def backup_router_config(device):
    try:
        # Establish SSH connection
        connection = ConnectHandler(**device)
        
        # Enter enable mode
        connection.enable()
        
        # Send command to get running config
        output = connection.send_command('show running-config')
        
        # Get the current date and time
        now = datetime.now()
        timestamp = now.strftime('%Y%m%d_%H%M%S')
        
        # Define backup file name and path
        backup_filename = f"backup_{device['host']}.txt"
        backup_filepath = os.path.join('standby', backup_filename)
        
        # Ensure backup directory exists
        os.makedirs('standby', exist_ok=True)
        
        # Write the running config to the backup file
        with open(backup_filepath, 'w') as backup_file:
            backup_file.write(output)
        
        print(f"Backup saved successfully to {backup_filepath}")
        
        # Close the connection
        connection.disconnect()
    
    except Exception as e:
        print(f"Failed to back up the router: {e}")

# Backup the router configuration
backup_router_config(cisco_device)
