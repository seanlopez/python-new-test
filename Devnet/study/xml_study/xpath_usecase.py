from lxml import etree

XML = '''
<data>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <GigabitEthernet>
                <name>1</name>
                <ip>
                    <address>
                        <dhcp/>
                    </address>
                </ip>
                <mop>
                    <enabled>false</enabled>
                    <sysid>false</sysid>
                </mop>
                <negotiation xmlns="http://cisco.com/ns/yang/Cisco-IOS-XEethernet">
                    <auto>true</auto>
                </negotiation>
            </GigabitEthernet>

            <GigabitEthernet>
                <name>2</name>
                <ip>
                    <address>
                        <primary>
                            <address>192.168.1.1</address>
                            <mask>255.255.255.0</mask>
                        </primary>
                    </address>
                </ip>
                <mop>
                    <enabled>false</enabled>
                    <sysid>false</sysid>
                </mop>
                <negotiation xmlns="http://cisco.com/ns/yang/Cisco-IOS-XEethernet">
                    <auto>true</auto>
                </negotiation>
            </GigabitEthernet>

        </interface>
    </native>
</data>
'''

par = etree.XML(XML)

print(par)
print(par.xpath("."))
print(par.xpath("./*/*/*"))

req =  par.xpath("./*/*/*", namespaces= {"j":"http://cisco.com/ns/yang/Cisco-IOS-XE-native"})
for i in req:
    tag = i.tag
    interface_id = i.xpath("./j:name", namespaces= {"j":"http://cisco.com/ns/yang/Cisco-IOS-XE-native"})
    print(interface_id)


'''
for ele in par.xpath("//ip/address/*"):
    if ele.tag == "dhcp":
        pass
    else:
        interface_type = ele.xpath("../../..")[0].tag
        num = ele.xpath("../../../name/text()")[0]
        ip_addr = ele.xpath("./address/text()")[0]
        mask = ele.xpath("./mask/text()")[0]
        print("interface {} {} : ip address - {} mask - {}".format(interface_type, num, ip_addr, mask))
'''


