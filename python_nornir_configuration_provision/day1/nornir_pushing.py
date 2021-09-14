from nornir import InitNornir
from nornir_netmiko import netmiko_send_command, netmiko_send_config
from nornir.core.task import Task, Result
import nornir_jinja2
from nornir_utils.plugins.functions import print_result
from time import *

start_time = time()
nr = InitNornir(config_file="./config.yaml")

#send_result = nr.run(netmiko_send_config, config_file='config_commands.cfg')
results = nr.run(netmiko_send_command, command_string="show ip interface bri")

#print_result(send_result)
print_result(results)

def do_task_func(task: Task) -> Result:
    return Result(
        host=task.host,
        result=f"{task.host.name}"
    )

results = nr.run(do_task_func)

print(results)
print_result(results)

end_time = time()
print(end_time-start_time)
