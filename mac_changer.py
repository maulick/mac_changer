import subprocess
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC Address")
    return parser.parse_args()

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

args = get_arguments()
change_mac(args.interface, args.new_mac)
