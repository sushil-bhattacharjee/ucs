from ucsmsdk.ucshandle import UcsHandle  # Import UcsHandle to connect to UCS Manager
from ucsmsdk.ucseventhandler import UcsEventHandle  # Correct import
from ucsmsdk.mometa.ls.LsServer import LsServer
from ucsmsdk.mometa.ls.LsServer import LsServerConsts

import time  # Import time for sleep function

end_script = False

def sp_associate_callback(mce):
    global end_script
    if mce.mo.assoc_state == LsServerConsts.ASSOC_STATE_ASSOCIATED:
        print("SP: " + mce.mo.dn + " Assoc Successful. assoc_state: " + mce.mo.assoc_state)
    elif mce.mo.assoc_state == LsServerConsts.ASSOC_STATE_FAILED:
        print("SP: " + mce.mo.dn + " Assoc Failed. assoc_state: " + mce.mo.assoc_state)
    end_script = True

def sp_associate_monitor(event_handle, mo):
    event_handle.add(managed_object=mo, prop="assoc_state",
                     success_value=[LsServerConsts.ASSOC_STATE_ASSOCIATED],
                     failure_value=[LsServerConsts.ASSOC_STATE_FAILED],
                     timeout_sec=600, call_back=sp_associate_callback)

# Connect to UCS Manager
ucs_handle = UcsHandle("10.1.10.5", "ucspe", "ucspe")  # Replace with actual UCS Manager IP, username, and password
ucs_handle.login()

# Initialize UcsEventHandle with the connection handle
event_handle = UcsEventHandle(ucs_handle)

# Create the service profile (replace with actual parameters)
new_sp = LsServer(parent_mo_or_dn="org-root", name="my-service-profile")

# Add the new service profile to UCS Manager
ucs_handle.add_mo(new_sp, modify_present=True)
ucs_handle.commit()

# Monitor the association process
sp_associate_monitor(event_handle, new_sp)

# Wait for the association to complete
while not end_script:
    time.sleep(5)

# Logout from UCS Manager
ucs_handle.logout()

