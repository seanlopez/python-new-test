pre_check_list = [
        "show ip interface brief",
        "show interfaces",
        "show arp detail"
        ]

show_interface_expectation = ([["interface", "counters","in_pkts"], ["interface", "counters", "out_pkts"]], [["not equals", "0"], ["not equals", "0"]])

show_interface_report_content = [{"connection": "or"}, {"compliant": "traffic has been passed, checking compliant", "non-compliant": "no traffic passed, checking non-compliant"}]


show_ip_interface_brief_expectation = ([["interface", "interface_status"]], [["equals", "Up"]])

show_ip_interface_brief_report_content = [{"compliant": "interface is up", "non-compliant": "interface is down"}]


ping_report_content = {"compliant": "is pingable", "non-compliant": "cannot be reached"}


arp_report_content = {"compliant": "(next hop) address is existed in arp table", "non-compliant": "cannot find in arp table"}

def interface_policy(expectation, raw_data, ignore_loop="False"):
    expectation = expectation
    raw_data = raw_data
    #print(raw_data)
    interfaces = raw_data.keys()
    interface_non_loop = []
    if ignore_loop == "True":
        for interface in interfaces:
            if "Loopback" not in interface and "Null" not in interface:
                interface_non_loop.append(interface)
        interfaces = interface_non_loop
    #print(interfaces)
    elements_num = len(expectation[0])
    elements = expectation[0]
    expectation_value = expectation[1]
    result = {}
    for i in range(elements_num):
        result[i]={}
        expectation_value_item = expectation_value[i]
        for interface in interfaces:
            value_path = elements[i]
            value_path[0] = interface
            value = ""
            for path_locate in value_path:
                if value_path.index(path_locate) == 0:
                    value = raw_data[path_locate]
                else:
                    value = value[path_locate]  # ---> interface inbound traffic
            result_pre = {}
            if expectation_value_item[0] == "not equals":
                if str(value) != expectation_value_item[1]:
                    result[i][interface] = "compliant"
                else:
                    result[i][interface] = "non-compliant"
            elif expectation_value_item[0] == "equals":
                if str(value) == expectation_value_item[1]:
                    result[i][interface] = "compliant"
                else:
                    result[i][interface] = "non-compliant"
    return result

def route_next_hop_address_list(raw_data, vrf_name="default", address_family="ipv4"):
    next_hop_add_list = []
    #print(raw_data)
    routes = raw_data["vrf"][vrf_name]["address_family"][address_family]["routes"]
    for route in routes.keys():
        next_hop = routes[route]["next_hop"]
        if "next_hop_list" not in next_hop.keys():
            continue
        else:
            next_hop_list = next_hop["next_hop_list"]
            for index in next_hop_list.keys():
                next_hop_add = next_hop_list[index]["next_hop"]
                next_hop_add_list.append(next_hop_add)
    return list(set(next_hop_add_list))

def arp_policy(raw_data, next_hop_add_list):
    raw_data = raw_data
    next_hop_add_list = next_hop_add_list
    all_interfaces_arp = raw_data["interfaces"]
    interfaces = all_interfaces_arp.keys()
    result = {}
    add_exist = []
    for interface in interfaces:
        interface_arp = all_interfaces_arp[interface]
        arp_items = interface_arp["ipv4"]["neighbors"]
        for next_hop in next_hop_add_list:
            if next_hop in arp_items.keys():
                result[next_hop] = "compliant"
                add_exist.append(next_hop)
            else:
                continue
    for i in add_exist: next_hop_add_list.remove(i)
    if len(next_hop_add_list) != 0:
        for next_hop in next_hop_add_list:
            result[next_hop] = "non-compliant"
    return result

def ping_policy(raw_data):
    raw_data = raw_data
    result = {}
    for ping_result_dict in raw_data:
        ip_add = ping_result_dict["ip_add"]
        success_rate = ping_result_dict["success_rate"]
        if success_rate != "0":
            result[ip_add] = "compliant"
        else:
            result[ip_add] = "non-compliant"
    return result


import json
import check_assessment

if __name__ == "__main__":
    '''
    f = open("/opt/pyats_share/output/test/testshowinterfaces", "r")
    raw_data = f.read()
    raw_data = json.loads(raw_data)
    #print(show_interface_policy(show_interface_expectation, raw_data))

    f1=open("/opt/pyats_share/output/test/testshowipinterfacebrief", "r")
    raw_data1 = f1.read()
    raw_data1 = json.loads(raw_data1)["interface"]
    #print(show_ip_interface_brief_policy(show_ip_interface_brief_expecation, raw_data1))
    result = interface_policy(show_ip_interface_brief_expectation, raw_data1)
    check_assessment.assessment_logic_report(raw_data, interface_policy, show_interface_expectation, "test_report", 
show_interface_report_content, "True")
    check_assessment.assessment_logic_report(raw_data1, interface_policy, show_ip_interface_brief_expectation, "test_report", 
show_interface_report_content, "True")
    '''
    f2 = open("/opt/pyats_share/output/show_route_test", "r")
    raw_data2 = json.loads(f2.read())
    f2.close()
    next_hop_address_list = route_next_hop_address_list(raw_data2, "default", "ipv4")
    check_assessment.assessment_logic_report_general(raw_data2, ping_policy, "test_ping_list_report", 
ping_report_content)

