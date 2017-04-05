#!/usr/bin/env python3.6

import detectusb

monThread = detectusb.MonitorThread()

while True:
	if detectusb.NewDevice == None:
		pass
	else:
		print(detectusb.NewDevice)
		detectusb.NewDevice = None
