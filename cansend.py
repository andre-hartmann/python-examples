#!/usr/bin/python3

# sudo pip3 install python-can
import can

bus = can.interface.Bus(channel = 'can0', bustype = 'socketcan')

msg = can.Message(0x123, data=[0x01, 0x02, 0x03, 0x04], is_extended_id=False)
bus.send(msg)

print("Message sent: " + str(msg))
