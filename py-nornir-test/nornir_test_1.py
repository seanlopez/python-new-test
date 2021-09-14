from nornir import InitNornir
from nornir.core.inventory import Host
from pprint import pprint

nr = InitNornir(config_file="config.yaml")
print(nr)
print(nr.config.runner.options["num_workers"])

print(nr.inventory.groups)
print(nr.inventory.hosts)

'''
print("-"*50 + "printer host schema" + "-"*50)
pprint(Host.schema(), indent=4)
'''
