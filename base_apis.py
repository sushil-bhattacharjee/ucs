# pylint: skip-file
from ucsmsdk.ucshandle import UcsHandle

# Login to UCS
handle = UcsHandle("10.1.10.5", "ucspe", "ucspe")
handle.login()

# Create the server using object sp with name SB_lab and template SBtemplate
# sp = LsServer(parent_mo_or_dn="org-root", name="SB_lab", src_templ_name="SBtemplate")
# handle.add_mo(sp)

"""The SDK provides APIs to enable CRUD operations.

Create an object - add_mo
Retrieve an object - query_dn,query_classid,query_dns,query_classids
Update an object - set_mo
Delete an object - delete_mo
"""

# handle.commit()

# Querying Objects via Distinguished Name (DN)
object = handle.query_dn("org-root/ls-SBtemplate")
# print(object)

####################################################################
# To query all the objects of Class ID computeBlade use this Python statement.
object_computeblade = handle.query_classid("computeBlade")
print("\nPrinting all computeBlade objects\n")
for obj in object_computeblade:
    # print(obj)
    print(f"Dn {obj.dn}, num of CPUs {obj.num_of_cpus}, num of cores {obj.num_of_cores}, "
          f"avi memory {obj.available_memory}, model {obj.model}, rackunit {obj.rn}")
    
####################################################################
# To query all the objects of Class ID computeBlade use this Python statement.
object_computerackunit = handle.query_classid("ComputeRackUnit")
print("\nPrinting all ComputeRackUnit objects\n")
for obj in object_computerackunit:
    # print(obj)
    print(f"Dn {obj.dn}, num of CPUs {obj.num_of_cpus}, num of cores {obj.num_of_cores}, "
          f"avi memory {obj.available_memory}, model {obj.model}, rackunit {obj.rn}")

####################################################################

    

