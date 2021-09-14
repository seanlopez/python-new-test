from master_sheet_edit.mongo_db_operation import MongoOperation
from stustu import master_sheet_operator
from tqdm import tqdm

def get_all_node_data(db_name):
    '''
    :param db_name: DB name
    :return: data list include all node and node loopback info
    '''
    global node_data
    conn = MongoOperation.MongoOperation()
    collection = conn.get_collection_1(db_name, "l3_interface_list")
    hostname_list = conn.get_hostname(db_name, "l3_interface_list", {"name":"system"})
    node_info_list = []
    for hostname in hostname_list:
        node_dic = {}
        for node in collection.find({"name":"system", "hostname":hostname}):
            node_data = {}
            node_data["hostname"] = node["hostname"]
            node_data["loopback_address"] = node["ip_addr"]
        node_dic[hostname] = node_data
        node_info_list.append(node_dic)
    return node_info_list

def get_all_port_data(db_name):
    conn = MongoOperation.MongoOperation()
    collection = conn.get_collection_1(db_name, "port_list")
    hostname_list = conn.get_hostname(db_name, "port_list")
    port_info_list = []
    for hostname in hostname_list:
        port_dict = {}
        port_info_all = []
        for port in collection.find({"hostname": hostname}):
            port_data = {}
            port_data["hostname"] = port["hostname"]
            port_data["physical_port"] = port["port_id"]
            port_data["service_mtu"] = port["mtu"]
            if "=" in port["descr"]:
                port_data["physical_description"] = "'" + port["descr"] + "'"
            else:
                port_data["physical_description"] = port["descr"]
            port_info_all.append(port_data)
        port_dict[hostname] = port_info_all
        port_info_list.append(port_dict)
    return port_info_list


def get_all_lag_interface(db_name):
    '''
    :param db_name: db_name
    :return: data list include all lag interface data
    '''
    conn = MongoOperation.MongoOperation()
    collection = conn.get_collection_1(db_name, "lag_list")
    hostname_list = conn.get_hostname(db_name, "lag_list")
    lag_interface_data_list = []
    for hostname in hostname_list:
        lag_dict = {}
        lag_data_all = []
        for lag_int in collection.find({"hostname": hostname}):
            lag_data = {}
            lag_data["hostname"] = lag_int["hostname"]
            lag_data["lag_interface"] = lag_int["lag_id"]
            lag_data["lag_interface_description"] = lag_int["descr"]
            member_ports = ""
            for mem in lag_int["member_ports"]:
                member_ports = member_ports + mem + ","
            lag_data["physical_port"] = member_ports
            lag_data["physical_description"] = lag_int["descr"]
            lag_data["lacp_mode"] = lag_int["lacp_mode"]
            lag_data_all.append(lag_data)
        lag_dict[hostname] = lag_data_all
        lag_interface_data_list.append(lag_dict)
    return lag_interface_data_list

def get_vpls_all(db_name, service_type):
    print("Retrieving vpls info from DB: ")
    conn = MongoOperation.MongoOperation()
    collection = conn.get_collection_1(db_name, "vpls_list")
    sdp_collection = conn.get_collection_1(db_name, "sdp_list")
    l3_collection = conn.get_collection_1(db_name, "l3_interface_list")
    hostname_list = conn.get_hostname(db_name, "vpls_list")
    vpls_data_list = []
    for hostname in tqdm(hostname_list):
        vpls_dict = {}
        vpls_data_all = []
        for vpls in collection.find({"hostname": hostname}):
            vpls_data = {}
            vpls_data["hostname"] = vpls["hostname"]
            if "sap" in vpls.keys():
                sap_list = vpls["sap"]
                interface = ""
                vlan = ""
                for sap in sap_list:
                    interface = interface + sap["ac_port"] + ", "
                    vlan = vlan + sap["ac_vlan"] + ", "
                vpls_data["interface"] = interface
                vpls_data["vlan"] = vlan
            vpls_data["vsi"] = str(vpls["pw_id"])
            vpls_data["pw_id"] = str(vpls["pw_id"])
            if "sdp" in vpls.keys():
                sdp_list = vpls["sdp"]
                peer_hostname = ""
                sdp_type = ""
                sdp_protocol = ""
                address = ""
                for sdp in sdp_list:
                    sdp_id = sdp["sdp_id"]
                    sdp_type = sdp_type + sdp["sdp_type"] + ", "
                    address_sub = ""
                    for sdp_content in sdp_collection.find({"id": sdp_id, "hostname": hostname}):
                        address_sub = address_sub + sdp_content["far_end"]
                        address = address + address_sub + ", "
                        sdp_protocol = sdp_protocol + sdp_content["proto"] + ", "
                    far_hostname_sub = ""
                    for far_hostname in l3_collection.find({"ip_addr": address_sub}):
                        far_hostname_sub = far_hostname_sub + far_hostname["hostname"]
                        break
                    if far_hostname_sub == "":
                        peer_hostname = peer_hostname + "None" + ", "
                    else:
                        peer_hostname = peer_hostname + far_hostname_sub + ","
                vpls_data["peer_hostname"] = peer_hostname
                vpls_data["sdp_type"] = sdp_type
                vpls_data["sdp_protocol"] = sdp_protocol
                vpls_data["address"] = address
            if "mac_move" in vpls.keys():
                vpls_data["mac_move"] = vpls["mac_move"]
            if "fdb_size" in vpls.keys():
                vpls_data["fdb_size"] = vpls["fdb_size"]
            for service in service_type.keys():
                if service in vpls["descr"]:
                    vpls_data["service_type"] = service_type[service]
                    break
            vpls_data_all.append(vpls_data)
        vpls_dict[hostname] = vpls_data_all
        vpls_data_list.append(vpls_dict)
    return vpls_data_list

def get_vpws_all(db_name, service_type):
    print("Retrieving vpws info from DB: ")
    conn = MongoOperation.MongoOperation()
    collection = conn.get_collection_1(db_name, "vpws_list")
    sdp_collection = conn.get_collection_1(db_name, "sdp_list")
    l3_collection = conn.get_collection_1(db_name, "l3_interface_list")
    hostname_list = conn.get_hostname(db_name, "vpws_list")
    vpws_data_list = []
    for hostname in tqdm(hostname_list):
        vpws_dict = {}
        vpws_data_all = []
        for vpws in collection.find({"hostname": hostname}):
            vpws_data = {}
            vpws_data["hostname"] = vpws["hostname"]
            vpws_data["interface"] = vpws["ac_port"]
            vpws_data["vlan"] = vpws["ac_vlan"]
            vpws_data["pw_id"] = str(vpws["pw_id"])
            if "sdp" in vpws.keys():
                if len(vpws["sdp"]) == 1:
                    primary_sdp_id = vpws["sdp"][0]["sdp_id"]
                    far_end_address = ""
                    far_end_hostname = ""
                    sdp_description = ""
                    for sdp in sdp_collection.find({"id":primary_sdp_id, "hostname": hostname}):
                        far_end_address = sdp["far_end"]
                        vpws_data["peer_address_primary"] = sdp["far_end"]
                        sdp_description = sdp["descr"]
                    for far_hostname in l3_collection.find({"ip_addr": far_end_address}):
                        far_end_hostname = far_hostname["hostname"]
                    if far_end_hostname == "":
                        vpws_data["peer_hostname_primary"] = sdp_description + "(peer description)"
                    else:
                        vpws_data["peer_hostname_primary"] = far_end_hostname
                else:
                    primary_sdp_id = vpws["sdp"][0]["sdp_id"]
                    secondary_sdp_id = vpws["sdp"][1]["sdp_id"]
                    far_end_address = ""
                    far_end_hostname = ""
                    for sdp in sdp_collection.find({"id": primary_sdp_id, "hostname": hostname}):
                        far_end_address = sdp["far_end"]
                        vpws_data["peer_address_primary"] = sdp["far_end"]
                    for far_hostname in l3_collection.find({"ip_addr": far_end_address}):
                        far_end_hostname = far_hostname["hostname"]
                    if far_end_hostname == "":
                        vpws_data["peer_hostname_primary"] = vpws["descr"] + "(peer description)"
                    else:
                        vpws_data["peer_hostname_primary"] = far_end_hostname

                    for sdp in sdp_collection.find({"id": secondary_sdp_id, "hostname": hostname}):
                        far_end_address = sdp["far_end"]
                        vpws_data["peer_address_secondary"] = sdp["far_end"]
                    for far_hostname in l3_collection.find({"ip_addr": far_end_address}):
                        far_end_hostname = far_hostname["hostname"]
                    if far_end_hostname == "":
                        vpws_data["peer_hostname_secondary"] = vpws["descr"] + "(peer description)"
                    else:
                        vpws_data["peer_hostname_secondary"] = far_end_hostname
            vpws_data["vpn_description"] = vpws["descr"]
            for service in service_type.keys():
                if service in vpws["descr"]:
                    vpws_data["service_type"] = service_type[service]
                    break
            vpws_data_all.append(vpws_data)
        vpws_dict[hostname] = vpws_data_all
        vpws_data_list.append(vpws_dict)
    return vpws_data_list

def get_all_vpws_logical_interface(db_name):
    print("Retrieving vpws logical interface info from DB: ")
    conn = MongoOperation.MongoOperation()
    collection = conn.get_collection_1(db_name, "vpws_list")
    hostname_list = conn.get_hostname(db_name, "vpws_list")
    logical_interface_data_list = []
    for hostname in tqdm(hostname_list):
        logical_interface_dict = {}
        logical_interface_data_all = []
        for vpws in collection.find({"hostname": hostname}):
            logical_interface_data = {}
            logical_interface_data["hostname"] = vpws["hostname"]
            logical_interface_data["interface"] = vpws["ac_port"]
            logical_interface_data["vlan_id"] = vpws["ac_vlan"]
            logical_interface_data["vpn_type"] = "vpws"
            logical_interface_data["service_mtu"] = vpws["mtu"]
            logical_interface_data["description"] = vpws["descr"]
            logical_interface_data_all.append(logical_interface_data)
        logical_interface_dict[hostname] = logical_interface_data_all
        logical_interface_data_list.append(logical_interface_dict)
    return logical_interface_data_list

def get_all_vpls_logical_interface(db_name):
    print("Retrieving vpls logical interface info from DB: ")
    conn = MongoOperation.MongoOperation()
    collection = conn.get_collection_1(db_name, "vpls_list")
    # sdp_collection = conn.get_collection_1(db_name, "sdp_list")
    # l3_collection = conn.get_collection_1(db_name, "l3_interface_list")
    hostname_list = conn.get_hostname(db_name, "vpls_list")
    logical_vpls_data_list = []
    for hostname in tqdm(hostname_list):
        logical_interface_dict = {}
        logical_interface_data_all = []
        for vpls in collection.find({"hostname": hostname}):
            if "sap" in vpls.keys():
                for sap in vpls["sap"]:
                    logical_interface_data = {}
                    logical_interface_data["hostname"] = vpls["hostname"]
                    logical_interface_data["interface"] = sap["ac_port"]
                    logical_interface_data["vlan_id"] = sap["ac_vlan"]
                    logical_interface_data["vpn_type"] = "vpls"
                    logical_interface_data["service_mtu"] = str(vpls["mtu"])
                    logical_interface_data["description"] = vpls["descr"]
                    if "ingress" in sap.keys():
                        logical_interface_data["qos_in"] = sap["ingress"]["ingress_qos"]
                        logical_interface_data["ingress_filter"] = sap["ingress"]["mac_filter"]
                        logical_interface_data["ingress_scheduler"] = sap["ingress"]["ingress_scheduler"]
                    if "egress" in sap.keys():
                        logical_interface_data["qos_out"] = sap["egress"]["egress_qos"]
                        logical_interface_data["egress_filter"] = sap["egress"]["mac_filter"]
                        logical_interface_data["egress_scheduler"] = sap["egress"]["egress_scheduler"]
                    logical_interface_data_all.append(logical_interface_data)
        logical_interface_dict[hostname] = logical_interface_data_all
        logical_vpls_data_list.append(logical_interface_dict)
    return logical_vpls_data_list


def nokia_bulk_insert(file_path,data_list, section_name, mode="merge"):
    data_list = data_list
    for data in tqdm(data_list):
        #print(data)
        for key in data.keys():
            #print(key)
            MS = master_sheet_operator.MasterSheet(file_path, key)
            insert_data = data[key]
            #print(insert_data)
            MS.bulk_insert(section_name, 0, insert_data, mode)
            MS.wb.save(file_path)


def nokia_single_insert(file_path, data_list, section_name):
    data_list = data_list
    for data in tqdm(data_list):
        for key in data.keys():
            MS = master_sheet_operator.MasterSheet(file_path, key)
            insert_data = data[key]
            MS.insert(section_name, 0, insert_data)
            MS.wb.save(file_path)

if __name__ == "__main__":
    service_type = {
        "ASTINET" : "ENT Internet LL",
        "IPVPN" : "ENT IPVPN",
        "VPNIP" : "ENT IPVPN",
        "FTTH-SIP" : "VoIP",
        "SIP-DCN" : "VoIP",
        "SIP GPON" : "VoIP",
        "VOIP" : "VoIP",
        "FTTH-VOICE" : "VoIP",
        "VOICE": "VoIP",
        "SIP-AREA" : "VoIP",
        "SIGNALING" : "Voice MSAN",
        "Voice_MSAN" : "Voice MSAN",
        "VOICE MSAN" : "Voice MSAN",
        "VOICE-MSAN" : "Voice MSAN",
        "SPEEDY HOTSPOT" : "Internet",
        "HSI" : "HSI",
        "IPTV" : "IPTV",
        "IPPBX" : "IPPBX",
        "WIFI" : "WIFI",
        "TELKOMSEL" : "MBH",
        "METRO" : "ENT L2 METRO",
        "INTMETRNOR" : "ENT L2 METRO"
    }
    node_list = get_all_node_data("tianqi_db")
    lag_interface_data_list = get_all_lag_interface("tianqi_db")
    port_info_list = get_all_port_data("tianqi_db")
    vpws_info_list = get_vpws_all("tianqi_db", service_type)
    vpls_info_list = get_vpls_all("tianqi_db", service_type)
    logical_vpws_info_list = get_all_vpws_logical_interface("tianqi_db")
    logical_vpls_info_list = get_all_vpls_logical_interface("tianqi_db")
    #print(port_info_list)
    print("Insert all Lag interface info to the master sheet: ")
    nokia_bulk_insert("C:\python-new-code\openpyxltest\master_sheet_edit\\PT_Telkom_Master_Sheet.xlsx", lag_interface_data_list, "Interface")
    print("Insert all node section data: ")
    nokia_single_insert("C:\python-new-code\openpyxltest\master_sheet_edit\\PT_Telkom_Master_Sheet.xlsx", node_list, "Node")
    print("Insert all port info to master sheet: ")
    nokia_bulk_insert("C:\python-new-code\openpyxltest\master_sheet_edit\\PT_Telkom_Master_Sheet.xlsx", port_info_list, "Interface")
    print("Insert all VPWS info to master sheet: ")
    nokia_bulk_insert("C:\python-new-code\openpyxltest\master_sheet_edit\\PT_Telkom_Master_Sheet.xlsx", vpws_info_list, "L2VPN_ELINE")
    print("Insert all VPLS info to master sheet: ")
    nokia_bulk_insert("C:\python-new-code\openpyxltest\master_sheet_edit\\PT_Telkom_Master_Sheet.xlsx", vpls_info_list, "L2VPN ELAN")
    print("Insert all VPWS logical interfaces info to master sheet: ")
    nokia_bulk_insert("C:\python-new-code\openpyxltest\master_sheet_edit\\PT_Telkom_Master_Sheet.xlsx", logical_vpws_info_list, "Logical Interface")
    print("Insert all VPLS logical interfaces info to master sheet: ")
    nokia_bulk_insert("C:\python-new-code\openpyxltest\master_sheet_edit\\PT_Telkom_Master_Sheet.xlsx", logical_vpls_info_list, "Logical Interface")
