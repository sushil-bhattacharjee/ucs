from ucsmsdk.ucshandle import UcsHandle
from rich import print
from ucsmsdk.utils.converttopython import convert_to_ucs_python
handle = UcsHandle("10.1.10.5", "ucspe", "ucspe")
handle.login()

blades = handle.query_classid("computeBlade")
print("\n[bold green]Query for all blades[/bold green]\n")
for blade in blades:
    print(blade.model, blade.serial, blade.dn, blade.total_memory, blade.num_of_cpus)
    
"""Query for the vlade model UCSB-B200-M6
"""

# Query for the blade model UCSB-B200-M6
print("\n[bold yellow]Query for the blade model UCSB-B200-M6[/bold yellow]\n")
blades = handle.query_classid("computeBlade", filter_str="(model, 'UCSB-B200-M6', type='eq')")
for blade in blades:
    print(blade.model, blade.serial, blade.dn, blade.total_memory, blade.num_of_cpus)
    

#Use a filter to only Query for blades with a specific attribute using a regular expression re.

print("\n[bold blue]Query for blades with a specific attribute using a regular expression re[/bold blue]\n")
blades = handle.query_classid("computeBlade", filter_str="(dn, 'blade-[1,3]', type='re')")
for blade in blades:
    print(blade.model, blade.serial, blade.dn, blade.total_memory, blade.num_of_cpus)
    
# Convert the captured log file to a Python script
print("\n[bold red]Convert the captured log file to a Python script[/bold red]\n")
convert_to_ucs_python(xml=True, literal_path="/home/sushil/ucs/MAC_POOL_OPS_PS_xmlReq.log")


handle.logout()