from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("10.1.10.4", "ucspe", "ucspe")
handle.login()
blades = handle.query_classid("computeBlade")
for blade in blades:
  print (blade.model, blade.serial, blade.dn, blade.total_memory, blade.num_of_cpus)