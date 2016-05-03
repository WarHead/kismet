#!/usr/bin/env python

import sys, KismetRest

if len(sys.argv) < 2:
    print "Expected server URI"
    sys.exit(1)

kr = KismetRest.Kismet(sys.argv[1])

kr.SetDebug(True)

# Get summary of devices
devices = kr.DeviceFilteredDot11Summary(sys.argv[2:])

if len(devices) == 0:
    print "No devices found"
    sys.exit(0)

# Print the SSID for every device we can.  Stupid print; no comparison
# of the phy type, no handling empty ssid, etc.
for d in devices:
    if not d['kismet.device.base.phyname'] == "IEEE802.11":
        continue

    k = d['kismet.device.base.key']
    ssid = kr.DeviceField(k, "dot11.device/dot11.device.last_beaconed_ssid")

    if ssid == "":
        continue

    print "MAC", d['kismet.device.base.macaddr'],
    print "Type", d['kismet.device.base.type'],
    print "Channel",d['kismet.device.base.channel'],
    print "SSID", ssid


