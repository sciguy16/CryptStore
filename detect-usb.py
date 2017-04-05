#!/usr/bin/env python3.6

"""
This part listens for udev events to detect insertion of le usb
"""

import pyudev
import os

class USBMonitor:
	def __init__(self):
		self.context = pyudev.Context()
		self.monitor = pyudev.Monitor.from_netlink(self.context)
		self.monitor.filter_by(subsystem='usb')
		self.monitor.start()

if __name__ == "__main__":
	print("Entering debug mode...")
	print("You just lost the game")
	usbMon = USBMonitor()
	for device in iter(usbMon.monitor.poll, None):
		print("something happened...")
		print(device)
		for prop in device.__iter__():
			print(prop,device.__getitem__(prop))
		with os.scandir("/dev/disk/by-id/") as ls:
			for entry in ls:
				if device.__getitem__("ID_SERIAL") in entry.name:
					print(entry.name)
			ls.close()
