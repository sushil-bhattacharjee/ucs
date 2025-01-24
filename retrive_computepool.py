from ucsmsdk.ucshandle import UcsHandle

# Connect to UCS Manager
handle = UcsHandle("10.1.10.5", "ucspe", "ucspe")
handle.login()

if (server_pools := handle.query_classid("ComputePool")):
    print("Server Pools in UCS Manager:")
    for pool in server_pools:
        print(f"  Name: {pool.name}, DN: {pool.dn}, Status: {pool.status}")
else:
    print("No server pools found in UCS Manager.")

handle.logout()
