# encoding:utf-8
# _*_ coding: utf-8 _*_
import psutil
import os
import wmi


def bytes2human(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n


def get_cpu_info():
    print('CPU\n------------------------------------------------------------------------')
    print ("cpu_percent:%7s" %str(psutil.cpu_percent(0.5)) + "%"),
    cpu_percent = psutil.cpu_percent(0.5)
    return cpu_percent


def pprint_ntuple(nt):
    for name in nt._fields:
        value = getattr(nt, name)
        print
        if name != 'percent':
            value = bytes2human(value)
        print('%-10s : %7s' % (name.capitalize(), value)),


def get_memory_info():
    print ('\n------------------------------------------------------------------------')
    print('MEMORY\n------------------------------------------------------------------------'),
    pprint_ntuple(psutil.virtual_memory()),
    print ('\n------------------------------------------------------------------------'),
    print('\nSWAP\n------------------------------------------------------------------------'),
    pprint_ntuple(psutil.swap_memory()),
    return psutil.virtual_memory().percent


def get_disk_info():
    print ('\n------------------------------------------------------------------------')
    print('Disk\n------------------------------------------------------------------------')
    templ = "%-17s %8s %8s %8s %5s%% %9s  %s"
    print(templ % ("Device", "Total", "Used", "Free", "Use ", "Type",
                   "Mount"))
    count = len(psutil.disk_partitions(all=False))
    i = 0
    j = 0
    disk_part = []
    disk_info = []
    # for i in range(count):
    #     disk_info.append(i)
    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                # skip cd-rom drives with no disk in it; they may raise
                # ENOENT, pop-up a Windows GUI error for a non-ready
                # partition or just hang.
                continue
        usage = psutil.disk_usage(part.mountpoint)
        print(templ % (
            part.device,
            bytes2human(usage.total),
            bytes2human(usage.used),
            bytes2human(usage.free),
            int(usage.percent),
            part.fstype,
            part.mountpoint))
        for i in range(1):
            disk_part.append(part.device.split(':')[0])
            disk_part.append(usage.percent)
        disk_info.append(disk_part)
        disk_part = []
    return disk_info


def get_sys_version():
    c = wmi.WMI()
    for sys in c.Win32_OperatingSystem():
        return sys


def get_ip():
    c = wmi.WMI()
    for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=1):
        return interface.IPAddress


def get_mac():
    for interface in wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=1):
        return interface.MACAddress


def monitor_all():
    get_cpu_info()
    get_memory_info()
    get_disk_info()
    get_ip()
    get_mac()
    get_sys_version()







