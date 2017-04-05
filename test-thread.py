#!/usr/bin/env python3.6

import detectusb


def usbCB(path):
	print(path)


monThread = detectusb.MonitorThread(usbCB)

while True:
		pass
