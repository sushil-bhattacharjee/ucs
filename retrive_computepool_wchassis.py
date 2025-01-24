from ucsmsdk.ucshandle import UcsHandle

# Connect to UCS Manager
handle = UcsHandle("10.1.10.5", "ucspe", "ucspe")
handle.login()


# Define server pools to query
SERVER_POOLS = ["devcore_pool2", "devcore_pool", "default"]

for pool in SERVER_POOLS:
    server_pool_dn = f"org-root/compute-pool-{pool}"
    if (server_pool := handle.query_dn(server_pool_dn)):
        print(f"Server Pool '{server_pool.name}' found with DN: {server_pool.dn}")
        if (pooled_slots := handle.query_children(in_dn=server_pool_dn)):
            print("  Servers in the pool:")
            for slot in pooled_slots:
                print(f"    Chassis ID: {slot.chassis_id}, Slot ID: {slot.slot_id}")
        else:
            print("  No servers found in the pool.")
    else:
        print(f"Server Pool '{pool}' does not exist.")

handle.logout()

