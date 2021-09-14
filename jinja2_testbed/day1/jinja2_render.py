from jinja2 import Template

f = open("../template/testbed.j2", "r", encoding="utf-8")

interface_template = Template(f.read(), keep_trailing_newline=True)

configuration_list = [
    {"interface_name": "g0/1", "vlan": "trunk"},
    {"interface_name": "g0/2", "vlan": "10"}
]

interface_configure = ""
for config in configuration_list:
    interface_configure = interface_configure + interface_template.render(
        interface_name = config["interface_name"],
        vlan = config["vlan"]
    )
f.close()

configure_output = open("configuration_out.txt", "w", encoding="utf-8")
configure_output.write(interface_configure)

