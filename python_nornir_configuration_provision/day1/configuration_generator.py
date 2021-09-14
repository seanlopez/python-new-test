
configuraiton_file = open("./config_commands.cfg", "w", encoding="utf-8")
configuraiton_file.write("router static \n")
configuraiton_file.write("maximum path ipv4 140000 \n")
configuraiton_file.write("address-family ipv4 unicast \n")

x = 0
for h in range(1, 255):
    for k in range(1, 255):
        x = x+1
        if x < 10:
            configuraiton_file.write("1."+str(h)+"."+str(k)+".0/24 "+"192.168."+str(k)+"."+str(h)+"\n")
        else:
            break
configuraiton_file.write("commit \n")
configuraiton_file.close()
