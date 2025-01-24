from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("10.1.10.4", "ucspe", "ucspe")

vlans = handle.query_classid("FabricVlan")

for vlan_mo in vlans:
  if vlan_mo.id != "1":
    handle.remove_mo(vlan_mo)

handle.commit()
# Disconnect from UCS Manager. Use this python statement.
handle.logout()