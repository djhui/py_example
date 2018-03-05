#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import wmi
Disk = wmi.WMI().Win32_LogicalDisk()
for info in Disk:
    print(info)