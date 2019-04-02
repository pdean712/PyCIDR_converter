from ipaddress import IPv4Network
import fileinput
import re
regexp = re.compile(r'((2[0-5]{2}|2[0-4]\d|1\d{2}|[1-9]\d|\d)\.){3}(2[0-5]{2}|2[0-4]\d|1\d{2}|[1-9]\d|\d)(/(3[012]|[12]\d|\d))?')
for line in fileinput.input():
    for word in line.split():
        if regexp.search(word):
            print(IPv4Network(word).network_address, IPv4Network(word).netmask)
        else:
            print((word),end=" ")
