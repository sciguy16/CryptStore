#!/usr/bin/env python3.6

"""
This part listens for udev events to detect insertion of le usb
"""

import pyudev
import os
import psutil
import time
import pathlib
import threading

NewDevice=None

class USBMonitor:
	def __init__(self):
		self.context = pyudev.Context()
		self.monitor = pyudev.Monitor.from_netlink(self.context)
		self.monitor.filter_by(subsystem='usb')
		self.monitor.start()

class MonitorThread(object):
	def __init__(self):
		self.usbMon = USBMonitor()
		thread = threading.Thread(target=self.run,args=())
		thread.daemon = True
		thread.start()
	def run(self):
		for device in iter(self.usbMon.monitor.poll, None):
			time.sleep(4)
			for prop in device.__iter__():
				if(prop == 'ID_SERIAL'):
					#print("prop is id serial")
					pval = device.__getitem__(prop)
					#print("serial",pval)
	#			print(type(prop),prop,device.__getitem__(prop))
					with os.scandir("/dev/disk/by-id/") as ls:
						for entry in ls:
					#		print("ls:",entry)
							if pval in entry.name:
								#print("entry name",entry.name)
								devpath = str(pathlib.Path("/dev/disk/by-id",entry.name).resolve())
								#print("device:",devpath)
								for p in psutil.disk_partitions():
									#print("device yay:",p.device)
									if p.device == devpath:
										#print(p.mountpoint)
										global NewDevice
										NewDevice = p.mountpoint
						ls.close()


