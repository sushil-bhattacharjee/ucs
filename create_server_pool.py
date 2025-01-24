"""
Python code using the UCS Python SDK is creating a server pool named "devcore_pool2" and populating the pool with 
all servers from chassis 3, and then the server pool is associated to existing Service Profile template "SBtemplate".
"""
from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.ls.LsRequirement import LsRequirement
from ucsmsdk.mometa.compute.ComputePool import ComputePool
from ucsmsdk.mometa.compute.ComputePooledSlot import ComputePooledSlot

handle = UcsHandle("10.1.10.5", "ucspe", "ucspe")
handle.login()

SERVER_POOL = ComputePool(parent_mo_or_dn="org-root", name="devcore_pool2")
handle.add_mo(SERVER_POOL, modify_present=True)

for blade in handle.query_classid("ComputeBlade", filter_str='(chassis_id, "3")'):
    SERVER = ComputePooledSlot(parent_mo_or_dn=SERVER_POOL, chassis_id=blade.chassis_id, slot_id=blade.slot_id)
    handle.add_mo(SERVER, modify_present=True)

handle.commit()

SP_TEMPLATE = LsRequirement(parent_mo_or_dn="org-root/ls-SBtemplate", name="devcore_pool2")
handle.add_mo(SP_TEMPLATE, modify_present=True)

handle.commit()
# Query for the server pool by its DN
if (server_pool := handle.query_dn("org-root/compute-pool-devcore_pool2")):
    print(f"Server Pool '{server_pool.name}' exists with the following details:")
    print(f"  DN: {server_pool.dn}")
    print(f"  Status: {server_pool.status}")
else:
    print("Server Pool 'devcore_pool2' does not exist.")

handle.logout()
