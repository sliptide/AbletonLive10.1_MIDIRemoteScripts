#Embedded file name: /Users/versonator/Jenkins/live/output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Launch_Control/__init__.py
#Started with the LaunchControl scripts from Novation.
from __future__ import absolute_import, print_function, unicode_literals
from .TouchOSC import TouchOSC
from _Framework.Capabilities import controller_id, inport, outport, CONTROLLER_ID_KEY, PORTS_KEY, NOTES_CC, SCRIPT

def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=4661, product_ids=[52], model_name=u'TouchOSC'),
     PORTS_KEY: [inport('TouchOSC Bridge', props=[NOTES_CC, SCRIPT]), outport('TouchOSC Bridge', props=[NOTES_CC, SCRIPT])]}

def create_instance(c_instance):
    return TouchOSC(c_instance)
