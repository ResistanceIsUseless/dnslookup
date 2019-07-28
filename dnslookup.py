import dns.resolver
import dns.ipv4
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l', "--list", help="List of dns names you want IP's for")
parser.add_argument('-o', "--output", help="Output file to save list")
args = parser.parse_args()

ip_list = [...]
subs = open(args.list, 'r', newline='')

if args.list:
    for host in subs:
            host = host.strip('\n',)
            host = host.strip('https://')
            host = host.strip('http://')
            # print(host)
            try:
                i = dns.resolver.query(host,'A' )
                #print(i.rrset.items[0])
                for item in i:
                    if not item in ip_list:
                        ip_list.append(item)
                        print(item)
            except Exception as error:
                a = error

if args.output:
    file = open(args.output, "w")
    for p in ip_list:
        file.write(str(p))
        file.write("\n")
    file.close()
