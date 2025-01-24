from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

handle = UcsHandle("10.1.10.5", "ucspe", "ucspe")

lan_cloud = handle.query_classid("FabricLanCloud")

vlan_mo = FabricVlan(parent_mo_or_dn=lan_cloud[0], name="VLAN100", id="100")
handle.add_mo(vlan_mo, True)
handle.commit()
print(f"VLAN {vlan_mo.name} created successfully")
print(lan_cloud[0])

