#!/usr/bin/env python3

"""
This part listens for udev events to detect insertion of le usb
"""

import pyudev

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
