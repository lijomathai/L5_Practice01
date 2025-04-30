import yaml
import pyeapi

file = open('vlans.yml', 'r')

pyeapi.load_config('eapi.conf')
vlan_dict = yaml.safe_load(file)

for switch in vlan_dict['switches']:
    # print(f"Connecting to {switch}")
    connect = pyeapi.connect_to(switch)
    vlan_api = connect.api('vlans')
    vlan_info = connect.run_commands(['show vlan'])
    # print(f"vlans info as {vlan_info} from {switch}")
    cmd_vlans_dict = vlan_info[0]['vlans']
    # print(f"for switch{switch}")
    for vlan in cmd_vlans_dict:
        vlan_id = vlan
        vlan_name = cmd_vlans_dict[vlan]['name']
        # print(cmd_vlans_dict[vlan]['name'])
        # print(f"VLAN ID of {vlan_id} with name {vlan_name}")
        if vlan == '10':
          print(f"deleting vlan {vlan_id} from {switch}")
          vlan_api.delete(vlan)
    else:
      print(f"vlan 10 doesnot exist in {switch}")
