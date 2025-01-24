# noinspection SpellCheckingInspection

"""Modifying UCS Manager object with the Python SDK for LEDs follow these steps:

Retrieve the objects with a query.
Modify the object.
Set the object in the handle with the method set_mo().
Commit the object with the handle method commit().
"""

from ucsmsdk.ucshandle import UcsHandle

handle = UcsHandle("10.1.10.5", "ucspe", "ucspe")
handle.login()

compute_resources = handle.query_classids("ComputeBlade", "ComputeRackUnit")

for class_name, resources in compute_resources.items():
    for compute_resource in resources:
        leds = handle.query_children(in_dn=compute_resource.dn, class_id="equipmentLocatorLed")
        previous_oper_state = leds[0].oper_state
        
        leds[0].admin_state = "off" if leds[0].oper_state == "on" else "on"
        handle.set_mo(leds[0])
        handle.commit()
        print( "dn:",compute_resource.dn,
            "led previous",previous_oper_state,
            "led current",leds[0].admin_state)
