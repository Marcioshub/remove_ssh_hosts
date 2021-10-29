import os, argparse

home = os.path.expanduser("~")
parser = argparse.ArgumentParser(description='This script removes hosts from saved ssh known_hosts file')
parser.add_argument("--hosts", nargs="*", help="Enter list of hosts to remove. Ex: rmyhosts --hosts 192.168.1.2 192.168.1.3 192.168.1.4", required=True)
args = parser.parse_args()

def remove_hosts():
    try:
        if not os.path.exists("{}/.ssh/known_hosts".format(home)):
            raise Exception("Cannot locate: {}/.ssh/known_hosts".format(home))
        else:
            if len(args.hosts) >= 1:
                # read known hosts file
                f = open("{}/.ssh/known_hosts".format(home), "r")
                known_hosts = f.readlines()
                f.close()

                # iterate and remove given ips from the args list
                for host in args.hosts:
                    for line in known_hosts:
                        if host == line.split(" ")[0]:
                            known_hosts.remove(line)

                # rewrite known_hosts file
                f = open("{}/.ssh/known_hosts".format(home), "w")
                f.write("".join(known_hosts))
                f.close()

                print("{}: have been removed from the hosts file".format(args.hosts))
            else:
                raise Exception("You must pass at least one ip address in command line arguments")
    except Exception as err:
        print(err)

if __name__ ==  "__main__":
    remove_hosts()