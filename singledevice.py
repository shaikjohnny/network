from netmiko import ConnectHandler
 
#First create the device object using a dictionary
CSR = {
    'device_type': 'cisco_ios',
    'ip': '10.100.96.80',
    'username': 'cisco',
    'password': 'ffappcc@aa'
}
 
# Next establish the SSH connection
net_connect = ConnectHandler(**CSR)
 
# Then send the command and print the output
#output = net_connect.send_command('show ip int brief')
output = net_connect.send_command('show runn bri')
print (output)
 
# Finally close the connection
net_connect.disconnect()