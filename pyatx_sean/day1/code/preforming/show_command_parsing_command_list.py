import sys
import os
from pyats.topology.loader import load
import json
import pre_check_components
import post_check_components

class command_list_perform(object):
    def __init__(self):
        self.dst_device_hostname = sys.argv[1]
        self.show_command_list = sys.argv[2]
        self.output_folder_name = sys.argv[3]

    def perform_parsing_command_list(self, dst_device_hostname="", output_folder_name="", testbed_file="", command_list=[]):
        if dst_device_hostname == "":
            dst_device_hostname = self.dst_device_hostname
        if output_folder_name == "":
            output_folder_name = self.output_folder_name
        
        os.system(f"mkdir /pyats/users/output/{output_folder_name}")
        testbed = load(f'/pyats/users/testbed_files/{testbed_file}')
        device = testbed.devices[dst_device_hostname]
        device.connect()
        for com in command_list:
            show_command_output = device.parse(com)
            output_name = output_folder_name+com.replace(" ","")
            self.output_storage(output_folder_name, output_name, show_command_output) 
        return output_name
    
    def output_storage(self, output_folder_name, output_name, output):
        output_file = open(f"/pyats/users/output/{output_folder_name}/{output_name}", "w", encoding="utf-8")
        output_file.write(json.dumps(output))
        output_file.close()

if __name__ == "__main__":
    pre_check_list = pre_check_components.pre_check_list
    post_check_list = post_check_components.post_check_list

    check_handler = command_list_perform()
    if check_handler.show_command_list == "pre-check":
        check_handler.perform_parsing_command_list(testbed_file="testbed1.yaml", command_list=pre_check_list)
    elif check_handler.show_command_list == "post-check":
        check_handler.perform_parsing_command_list(testbed_file="testbed1.yaml", command_list=post_check_list)



