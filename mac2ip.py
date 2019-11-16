import re, subprocess


def mac2ip(mac):
    macip = re.compile(r'(([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})(\s*)(([0-9a-f]{2}-){5}[0-9a-f]{2}))')
    ARP = subprocess.Popen("arp -a", stdout=subprocess.PIPE)
    out = ARP.communicate()[0].decode("cp1251")
    macips = re.findall(macip, out)
    ret = {}
    for mi in macips:
        mi2 = re.split(r'\s*', mi[0])
        ret[mi2[1]] = mi2[0]
    if mac in ret.keys():
        return ret[mac.replace(':', '-')]
    else:
        return '-1'


def ip2mac(ip):
    macip = re.compile(r'(([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})(\s*)(([0-9a-f]{2}-){5}[0-9a-f]{2}))')
    ARP = subprocess.Popen("arp -a", stdout=subprocess.PIPE)
    out = ARP.communicate()[0].decode("cp1251")
    macips = re.findall(macip, out)
    ret = {}
    for mi in macips:
        mi2 = re.split(r'\s*', mi[0])
        ret[mi2[0]] = mi2[1]
    if ip in ret.keys():
        return ret[ip].replace('-', ':')
    else:
        return '-1'

