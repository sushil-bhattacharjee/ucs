# pylint: skip-file
from ucsmsdk.mometa.ls.LsServer import LsServer
from ucsmsdk.ucshandle import UcsHandle

# Login to UCS
handle = UcsHandle("10.1.10.5", "ucspe", "ucspe")
handle.login()

# Create the server using object sp with name SB_lab and template SBtemplate
sp = LsServer(parent_mo_or_dn="org-root", name="SB_lab", src_templ_name="SBtemplate")
handle.add_mo(sp)
handle.commit()