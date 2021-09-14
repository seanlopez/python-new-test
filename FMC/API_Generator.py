name = ["motac",
"kats",
"moa1",
"moa2",
"tourism1",
"tourism2",
"tourism3",
"tourism4",
"tourism5",
"tourism6",
"tourism7",
"tourism8",
"Pengarah_JPPM",
"ROS1",
"tourism9",
"JKSM_SR-CF-1060"]

value = ["10.17.146.21/32",
"10.19.125.149/32",
"10.19.82.6/32",
"10.19.82.7/32",
"10.17.156.126/32",
"10.17.156.43/32",
"10.17.156.60/32",
"10.17.156.61/32",
"10.17.156.62/32",
"10.17.156.63/32",
"10.17.156.64/32",
"10.17.156.65/32",
"10.21.129.75/32",
"10.21.129.44/32",
"10.17.156.19/32",
"10.25.150.53/22"]

f1 = open("CATALINA_IOS_Network.txt", "w", encoding="utf-8")
f2 = open("CATALINA_IOS_Host.txt", "w", encoding="utf-8")

for i in range(len(name)):
    name_loop = name[i]
    value_loop = value[i]
    if value_loop[-3] != "/" or int(value_loop[-1])*int(value_loop[-2]) == 6:
        f2.write('{\n "name":"CATALINA_IOS_' + name_loop + '",\n "value": "' + value_loop + '",\n "overridable": false,\n "description": "internal Trusted",\n "type": "host"\n},\n')
    else:
        f1.write('{\n "name":"CATALINA_IOS_' + name_loop + '",\n "value": "' + value_loop + '",\n "overridable": false,\n "description": "Franking",\n "type": "network"\n},\n')

f1.close()
f2.close()
