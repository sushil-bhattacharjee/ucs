from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("10.1.10.4", "ucspe", "ucspe")

from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

lan_cloud = handle.query_classid("FabricLanCloud")

vlans = ["200", "201", "202"]

for vlan in vlans:
  vlan_mo = FabricVlan(parent_mo_or_dn=lan_cloud[0], name="vlan"+vlan, id=vlan)
  handle.add_mo(vlan_mo, True)

handle.commit()