import subprocess
import argparse
import re

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC Address")
    args = parser.parse_args()
    if not args.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not args.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")
    return args

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    
def get_currnet_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC Address.")

args = get_arguments()
current_mac = get_current_mac(args.interface)
print("Current MAC = " + str(current_mac))
#change_mac(args.interface, args.new_mac)
