"""
this file include all ttp template for nokia
"""

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# OSPF TTP
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
<group = ospf>
    ospf_process_id
    <group = area>
        area_id
        interface:
            <group = interface>
                interface-type
                authentication-type
                message-digest-key-hash
                mtu
                metric
                interface status 
            </group>
    </group>
</group>
'''

ospf_ttp = '''
#--------------------------------------------------{{ignore}}
echo "OSPFv2 Configuration"{{_start_}}
#--------------------------------------------------{{ignore}}
<group name="ospfv2">
        ospf {{ospf_pid}}
        <group name = "area">
            area {{area_id}}
            <group name = "interface">
                interface "{{interface_name}}"
                    interface-type {{interface_type}}
                    authentication-type {{authentication_type}}
                    message-digest-key 1 md5 "{{authentication_key_hash}}" hash2
                    mtu {{mtu}}
                    metric {{metric}}
                    {{interface_shutdown | re("shutdown")}}
                    {{interface_shutdown | re("no shutdown")}}
            </group>
            </group>
    </group>
        exit{{_end_}}
'''
