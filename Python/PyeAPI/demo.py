import pyeapi
from pprint import pprint

pyeapi.load_config('eapi.conf')

node = pyeapi.connect_to('leaf1')
commands = ['show version', 'show ip route']
response = node.enable(commands)
pprint(response)

    # config_commands = ['configure terminal', 'vlan 123', 'name my_vlan', 'exit']
    # config_response = node.config(config_commands)
    # pprint(config_response)