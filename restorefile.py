from netmiko import ConnectHandler
import os

# Define the device details
cisco_device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',  # Replace with your router's IP address
    'username': 'admin',  # Replace with your router's username
    'password': 'password',  # Replace with your router's password
    'secret': 'secret',  # Enable password if required
}

def restore_router_config(device, backup_file):
    try:
        # Establish SSH connection
        connection = ConnectHandler(**device)
        
        # Enter enable mode
        connection.enable()
        
        # Read the backup file content
        with open(backup_file, 'r ') as file:
            config_commands = file.read().splitlines()
        
        # Enter configuration mode
        connection.send_config_set(config_commands)
        
        print(f"Configuration restored successfully from {backup_file}")
        
        # Save the configuration
        connection.save_config()
        
        # Close the connection
        connection.disconnect()
    
    except Exception as e:
        print(f"Failed to restore the router configuration: {e}")

# Path to the backup file
backup_file_path = 'path/to/your/backup_file.txt'  # Replace with the actual path to your backup file

# Restore the router configuration
restore_router_config(cisco_device, backup_file_path)
