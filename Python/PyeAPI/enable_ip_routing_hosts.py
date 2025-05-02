import pyeapi
import os
from pprint import pprint

pyeapi.load_config('eapi.conf')

host_pc = ['host1','host2']

for host in host_pc:
    connect = pyeapi.connect_to(host)
    node = pyeapi.connect_to(host)
    config_commands = ['configure terminal', 'ip routing', 'exit']
    config_response = node.config(config_commands)
    pprint(config_response)