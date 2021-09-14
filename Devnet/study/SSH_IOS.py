from netmiko import ConnectHandler
import warnings

warnings.filterwarnings("ignore")
device = {
    "device_type" : "cisco_ios",
    "ip" : "192.168.17.140",
    "username" : "cisco",
    "password" : "cisco",
    "secret" : "cisco"
}

ssh_connection = ConnectHandler(**device)


ssh_connection.enable()

#command_list = ["interface e0/1", "shutdown"]
#print(ssh_connection.send_config_set(command_list))
print(ssh_connection.send_command("show run"))
