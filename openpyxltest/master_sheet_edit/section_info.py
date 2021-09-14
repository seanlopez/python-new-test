"""
Return 1 dict:
    1 dict>. for section 2 titles
"""

section_name = ["Site", "Node", "Interface", "Logical Interface", "VRF", "Static Route", "L2VPN ELINE", "L2VPN ELAN", "L3VPN", "Multicast", "DHCP Pool", "DHCP Server", "DHCP Server Interface", "DHCP Relay"]

section_detail = [
    {
        "Site":
            {
             0:["hostname", "site_name"],
             1:["hostname", "site_name"]
            }
    },
    {
        "Node":
            {
             0:["hostname","loopback_address"],
             1:["hostname","loopback_address"]
            }
     },
    {
        "Interface":
            {
                0:["hostname", "lag_interface", "lag_interface_description", "physical_port", "speed", "service_mtu", "physical_description", "lacp_mode"],
                1:["hostname", "bundle_interface", "bundle_interface_description", "physical_port", "speed", "service_mut", "physical_description", "lacp_mode"]
            }
    },
    {
        "Logical Interface":
            {
                0:["hostname", "interface", "vlan_id", "vpn_type", "service_mtu", "bvi_int", "vpn_vsi_name", "ip_address", "qos_in", "qos_out", "description", "egress_filter", "ingress_filter", "egress_scheduler", "ingress_scheduler"],
                1:["hostname", "interface", "vlan_id", "vpn_type", "service_mtu", "bvi_int", "vpn_vsi_name", "ip_address", "qos_in", "qos_out", "description", "egress_filter", "ingress_filter", "qos_policy"]
            }
    },
    {
        "VRF":
            {
                0:["hostname", "vrf", "import_rt", "export_rt", "rpl_in", "rpl_out"],
                1:["hostname", "vrf", "import_rt", "export_rt", "rpl_in", "rpl_out", "customer_name", "customer_abbr", "enterprise_infra"]
            }
    },
    {
        "Static route":
            {
                0:["hostname", "vrf", "address_family", "subnet", "mask", "next_hop", "outgoing_interface"],
                1:["hostname", "vrf", "address_family", "subnet", "mask", "next_hop", "outgoing_interface"]
            }
    },
    {
        "L2VPN_ELINE":
            {
                0:["hostname", "interface", "vlan", "service_type", "src_int_type", "peer_hostname_primary", "peer_address_primary", "peer_hostname_secondary", "peer_address_secondary","peer_ac", "pw_id", "vpn_description"],
                1:["hostname", "interface", "vlan", "service_type", "src_int_type", "peer_hostname_primary", "peer_address_primary", "peer_hostname_secondary", "peer_address_secondary","peer_ac", "peer_ac_vlan", "pw_id", "xconnect_group_name", "p2p_service_name", "vpn_description"]
            }
    },
    {
        "L2VPN ELAN":
            {
                0:["hostname", "interface", "vlan", "vsi", "pw_id", "peer_hostname", "sdp_type", "sdp_protocol", "address", "service_type", "mac_move", "fdb_size"],
                1:["hostname", "interface", "vlan", "bg_name", "pw_id", "pw_id", "bd_name", "peer_hostname", "peer_address", "peer_protocol", "evpn_consolidation", "interface_description", "remote_pe_int_description", "remote_qos_in", "remote_qos_out", "vpn_description", "secure_login", "mac_limit"]
            }
    },
    {
        "L3VPN":
            {
                0:["hostname", "pim_interface", "vrf", "static_group", "static_group_source"],
                1:["hostname", "pim_interface", "vrf", "static_group", "static_group_source"]
            }
    }
]
