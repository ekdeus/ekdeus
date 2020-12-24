
#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
    parser = optparse. OptionParser()
    parser.add_option ("-i", "--interface", dest="interface", help="Interface to change its MAC add")
    parcer.add_option ("-m", "--mac", dest="new_mac", help="New MAC address")(options, arguments) = parser.parse_args())
    if not options.interface:
        parcer.error("[-] PLease specify an intrface, use --help for more info.")
    elif not options.new_mac
        parcer.error("[-] PLease specify an intrface, use --help for more info.")
    return options

def change_mac (interface, new_mac):
print("[+] Chaning MAC address for " + interface + " to " + new_mac)
subprocess.call("ifconfig wlan0 down", shell=True)
subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:55", shell=True)
subprocess.call("ifconfig wlan0 up", shell=True)

ifconfig_result = subprocess.check_output (["ifconfig", options.interface])
print (ifconfig_result)
# получение любой инфы - регулярные выражения pythex.org для создания правил для регулярных выражений
