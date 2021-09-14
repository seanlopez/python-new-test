import sys
import docker
import time
import os

class atscontroller(object):
    def __init__(self, container_id):
        '''
        :param container_id: import container ID

        init client and init pyats container
        '''

        self.client = docker.from_env()
        self.pyats_container = self.client.containers.get(container_id)

    def get_all_check_result(self, dst_device_hostname, check_type):
        '''
        :param dst_device_hostname: specify which device required to preform the pre-check
        :return: store all out_put file to a specific folder (the name should be "dst_device_hostname+_+timestamp")
        '''
        output_folder_name = self.output_folder_name(dst_device_hostname)
        self.rewrite_shell_script(dst_device_hostname, check_type, output_folder_name, "show_command_parsing_command_list.py ")
        self.pyats_container.exec_run("bash /pyats/users/code/shell_controller/launch_ats.sh")
        return output_folder_name

    def specific_check_result(self, dst_device_hostname, show_command, option="False"):
        '''
        :param dst_device_hostname:
        :param show_commands: perform specific show command on dst_device
        :return: if the show command can be parsed, return paring file, if not, return the command return directly
        '''
        if option == "False":
            output_name = self.output_folder_name(dst_device_hostname) + show_command.replace(" ","")
            self.rewrite_shell_script(dst_device_hostname, show_command, output_name, "show_command_parsing.py")
            self.pyats_container.exec_run("bash /pyats/users/code/shell_controller/launch_ats.sh")
            return output_name
        elif option == "True1":
            output_name = self.output_folder_name(dst_device_hostname) + show_command.replace(" ","")
            self.rewrite_shell_script(dst_device_hostname, show_command, output_name, "show_command_parsing.py", "True1")
            self.pyats_container.exec_run("bash /pyats/users/code/shell_controller/launch_ats.sh")
            return output_name
        elif option == "True2":
            pass
        elif sys.argv[1] == "pre-ping":
            output_name = self.output_folder_name(dst_device_hostname) + show_command.replace(" ","") + "pre-ping-test"
            self.rewrite_shell_script(dst_device_hostname, show_command, output_name, "show_command_parsing.py", "True", "pre-ping")
            self.pyats_container.exec_run("bash /pyats/users/code/shell_controller/launch_ats.sh")
        elif sys.argv[1] == "post-ping":
            pass

    def delete_output(self, output_name):
        os.system(f"rm -rf {output_name}")

    def rewrite_shell_script(self, dst_device_hostname, show_command, output_name, specific_py_script, option="False", check_type = "pre-check"):
        '''
        rewrite the launch shell script, to guide the pyATS run specific python script in ATS
        :param dst_device_hostname:
        :param specific_py_script:
        :param show_command:
        :param output_name:
        :return:
        '''
        shell_script = open("/opt/pyats_share/code/shell_controller/launch_ats.sh", "w", encoding="utf-8")
        shell_script.write("#! /bin/bash \nsource bin/activate \n")
        shell_script.write(f"python3 /pyats/users/code/performing/{specific_py_script} {dst_device_hostname} '{show_command}' {output_name} {option} {check_type}")
        shell_script.close()

    def output_folder_name(self, dst_device_hostname):
        '''
        :param dst_device_hostname:
        :return: return folder name
        '''
        timestamp = time.strftime('%Y%m%d%H%M%S')
        return dst_device_hostname + "_" + timestamp

if __name__ == "__main__":
    docker_control = atscontroller("cef419080c91")
    if sys.argv[1] == "specific-show":
        show_command = sys.argv[2]
        docker_control.specific_check_result("cisco-ios-xr-01", show_command, "False")
    elif sys.argv[1] == "pre-check":
        docker_control.get_all_check_result("cisco-ios-xr-01", "pre-check")
    elif sys.argv[1] == "post-check":
        docker_control.get_all_check_result("cisco-ios-xr-01", "post-check")
    elif sys.argv[1] == "pre-specific-show-analysis":
        show_command = sys.argv[2]
        docker_control.specific_check_result("cisco-ios-xr-01", show_command, "True1")
    elif sys.argv[1] == "post-specific-show-analysis":
        show_command = sys.argv[2]
        docker_control.specific_check_result("cisco-ios-xr-01", show_command, "True2")
    elif sys.argv[1] == "pre-ping":
        show_command = sys.argv[2]
        vrf_name = sys.argv[3]
        docker_control.specific_check_result("cisco-ios-xr-01", show_command, vrf_name)
    else:
        print(f"Please use correct command, no command '{sys.argv[1]}'")
        exit()
    print("Checking Complete, please check the report in '/opt/pyats_share/output/' folder!!")



