def ssh_connect(device_type,ip, username, password, enable_password):
    from netmiko import ConnectHandler
    import warnings

    warnings.filterwarnings("ignore")
    device = {
        "device_type": device_type,
        "ip": ip,
        "username": username,
        "password": password,
        "secret": enable_password
    }

    return ConnectHandler(**device)

'''
def command(func):
    coms = input("please enter your commands/command, use comma to separate each command: ")
    coms = coms.split(",")
    ssh_connection = func
    ssh_connection.enable()
    if len(coms) != 1:
        # command_list = ["interface e0/1", "shutdown"]
        # print(ssh_connection.send_config_set(command_list))
        print(ssh_connection.send_config_set(coms))
    else:
        coms_fir = coms[0]
        if coms_fir.split(" ")[0] == "show":
            print(ssh_connection.send_command(coms[0]))
        else:
            print(ssh_connection.send_config_set(coms))
'''

def upload_config(file_name):
    com_set = []
    f = open(file_name, "r" )
    com_set_temp = f.readlines()
    f.close()
    for i in com_set_temp:
        com_set.append(i.split("\n")[0])
    return com_set

def save_info(output, file_name):
    f = open(file_name, "w")
    i = 0
    for line in output:
        i = i+1
        if i < len(output):
            f.write(line+"\n")
        else:
            f.write(line)
    f.close()

def save_info_append(output, file_name):
    f = open(file_name, "a+")
    i = 0
    for line in output:
        i = i+1
        if i < len(output):
            f.write(line+"\n")
        else:
            f.write(line)
    f.write("\n\n")
    f.close()

def configure_command(com_set, handler):
    ssh_connect1 = handler
    ssh_connect1.enable()
    ssh_connect1.send_config_set(com_set)

def show_command(show_com, handler):
    ssh_connect1 = handler
    ssh_connect1.enable()
    output = ssh_connect1.send_command(show_com)
    output = output.split("\n")
    return output


if __name__ == '__main__':
    sw_connection = ssh_connect("cisco_ios", "192.168.17.140", "cisco", "cisco", "cisco")
    fw_connection = ssh_connect("cisco_asa", "192.168.17.145", "cisco", "cisco", "cisco")

    com_set_sw = upload_config("./configure_file_switch.txt")
    configure_command(com_set_sw, sw_connection)

    com_set_fw = upload_config("./configure_file_ASA.txt")
    configure_command(com_set_fw,fw_connection)


    list_sw = show_command("show run", sw_connection)
    save_info(list_sw, "./switchconfiguration.txt")

    list_fw = show_command("show run", fw_connection)
    save_info(list_fw, "./asaconfiguration.txt")

    arp_sw = show_command("show arp", sw_connection)
    arp_fw = show_command("show arp", fw_connection)
    save_info_append(arp_sw, "./arp.txt")
    save_info_append(arp_fw, "./arp.txt")

    sw_connection.disconnect()
    fw_connection.disconnect()

    print("all task are completed!")

