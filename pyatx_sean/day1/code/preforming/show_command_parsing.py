import sys
import os
from pyats.topology.loader import load
import json
import pre_check_components
from parsing_template import ttp_parsing
from ttp import ttp
import check_assessment


class show_command_perform(object):
    def __init__(self):
        self.dst_device_hostname = sys.argv[1]
        self.show_command = sys.argv[2]
        self.output_name = sys.argv[3]
        self.option = sys.argv[4]
        self.check_type = sys.argv[5]

    def perform_parsing(self, dst_device_hostname="", show_command="", output_name="", testbed_file=""):
        if dst_device_hostname == "":
            dst_device_hostname = self.dst_device_hostname
        if show_command == "":
            show_command = self.show_command
        if output_name == "":
            output_name = self.output_name

        testbed = load(f'/pyats/users/testbed_files/{testbed_file}')
        device = testbed.devices[dst_device_hostname]
        device.connect()
        show_command_output = device.parse(show_command)
        self.output_storage(output_name, show_command_output) 
        return show_command_output

    def perform_show_2_file(self, dst_device_hostname="", show_command="", output_name="", testbed_file=""):
        if dst_device_hostname == "":
            dst_device_hostname = self.dst_device_hostname
        if show_command == "":
            show_command = self.show_command
        if output_name == "":
            output_name = self.output_name

        testbed = load(f'/pyats/users/testbed_files/{testbed_file}')
        device = testbed.devices[dst_device_hostname]
        device.connect()
        show_command_output = device.execute(show_command)
        self.output_storage_string(output_name, show_command_output)
        return show_command_output

    def perfrom_ping(self, address, dst_device_hostname="", show_command="", output_name="", testbed_file=""):
        address = address
        if dst_device_hostname == "":
            dst_device_hostname = self.dst_device_hostname
        if output_name == "":
            output_name = self.output_name

        testbed = load(f'/pyats/users/testbed_files/{testbed_file}')
        device = testbed.devices[dst_device_hostname]
        device.connect()
        output = open(f"/pyats/users/output/{output_name}", "w", encoding="utf-8")
        for add in address:
            print(add)
            show_command_output = device.execute(f"ping ipv4 {add}")
            output.write(f"ping ipv4 {add} \n")
            output.write(show_command_output)
            output.write("\n")
        output.close()
        return f"/pyats/users/output/{output_name}"


    def customization_parsing(self, template, raw_file):
        f = open(raw_file, "r")
        raw_string = f.read()
        f.close()
        parser = ttp(data=raw_string, template=template)
        parser.parse()
        result = parser.result(format='json')[0]
        result = json.loads(result)
        try:
            result = result[0]
        except Exception as e:
            if raw_string == "":
                print("Error:  Inputed an empty string")
            else:
                print("input error, the parsing raw_data is : "+ raw_string)
        return result
    
    def output_storage(self, output_name, output):
        output_file = open(f"/pyats/users/output/{output_name}", "w", encoding="utf-8")
        output_file.write(json.dumps(output))
        output_file.close()

    def output_storage_string(self, output_name, output):
        output_file = open(f"/pyats/users/output/{output_name}", "w", encoding="utf-8")
        output_file.write(output)
        output_file.close()

if __name__ == "__main__":
    parsing_list = [
            "show install active summary",
            "show install committed summary",
            "show inventory",
            "show platform",
            "show processes cpu",
            "show redundancy",
            "show version",
            "show route ipv4",
            "show bgp ipv4 labeled-unicast summary",
            "show bgp ipv4 mvpn summary",
            "show bgp l2vpn evpn summary",
            "show bgp link-state link-state summary",
            "show bgp vpnv4 unicast summary",
            "show bgp vpnv6 unicast summary",
            "show interfaces",
            "show ip interface brief",
            "show isis neighbors",
            "show arp detail"
            ]
    show_com = show_command_perform()
    if show_com.option == "False":
        if show_com.show_command in parsing_list:
            output = show_com.perform_parsing(testbed_file="testbed1.yaml")
        else:
            show_com.perform_show_2_file(testbed_file="testbed1.yaml")
    elif show_com.option == "True1":
        if show_com.show_command in pre_check_components.pre_check_list:
            output = show_com.perform_parsing(testbed_file="testbed1.yaml")
            report_name = "users/output/" + show_com.output_name + "human_report"
            if show_com.show_command == "show ip interface brief":
                check_assessment.assessment_logic_report_interface(output["interface"], pre_check_components.interface_policy, pre_check_components.show_ip_interface_brief_expectation, report_name, pre_check_components.show_ip_interface_brief_report_content)
            elif show_com.show_command == "show interfaces":
                check_assessment.assessment_logic_report_interface(output, pre_check_components.interface_policy, pre_check_components.show_interface_expectation, report_name, pre_check_components.show_interface_report_content, ignore_loop="True")
            elif show_com.show_command == "show arp detail":
                show_raw_file =  show_com.perform_parsing(show_command="show route ipv4", testbed_file="testbed1.yaml")
                address_list = pre_check_components.route_next_hop_address_list(show_raw_file)
                check_assessment.assessment_logic_report_general(output, pre_check_components.arp_policy, report_name, pre_check_components.arp_report_content, option=address_list)
        else:
            print(f"{show_com.show_command} cannot be analyzed")
    elif show_com.option == "True2":
        pass
    elif show_com.check_type == "pre-ping":
        show_raw_file =  show_com.perform_parsing(testbed_file="testbed1.yaml")
        address_list = pre_check_components.route_next_hop_address_list(show_raw_file)
        ping_result = show_com.perfrom_ping(address = address_list, testbed_file="testbed1.yaml")
        ping_result_parsing = show_com.customization_parsing(ttp_parsing.ping_parsing_template, ping_result)
        report_name = "users/output/" + show_com.output_name + "human_report"
        check_assessment.assessment_logic_report_general(ping_result_parsing, pre_check_components.ping_policy, report_name, pre_check_components.ping_report_content)
