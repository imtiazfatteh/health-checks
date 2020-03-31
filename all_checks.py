#!/usr/bin/env python3

import os
import shutil

def check_reboot():
  return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_absolute, min_percent):
  du = shutil.disk_usage(disk)
  percent_free = 100*du.free/du.total
  gigabytes_free = du.fre/2**30
  if percent_free < min_percent or gigabytes_free < min_absolute:
    return Ture
  return False

def main():
  if check_reboot():
    print("Pending Reboot.")
    sys.exit(1)
  if check_disk_full("/", 2, 10):
    print("Disk Full.")
    sys.exit(1)
  else:
    print("Everything ok.")
    sys.exit(0)

main()
