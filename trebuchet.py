"""

    )               )                )           )
 ( /( (      (   ( /(    (        ( /(    (   ( /(
 )\()))(    ))\  )\())  ))\   (   )\())  ))\  )\())
(_))/(()\  /((_)((_)\  /((_)  )\ ((_)\  /((_)(_))/
| |_  ((_)(_))  | |(_)(_))(  ((_)| |(_)(_))  | |_
|  _|| '_|/ -_) | '_ \| || |/ _| | ' \ / -_) |  _|
 \__||_|  \___| |_.__/ \_,_|\__| |_||_|\___|  \__|

Usage:
    trebuchet.py [--host=<hostname>] [--host_list=<path-to-txt>] [--port=<port_number>] [--use_https=<True/False>]
    trebuchet.py (-h | --help)
Arguments:
    host: The base host www.site.com
    host_list: The list used for brute-forcing
    port_number: The port used by the scanner
    use_https: Takes a boolean
"""

from docopt import docopt
from modules.enumerator import enumerate_virtual_hosts


__version__ = "0.5.0"
__author__ = "Shane Caldwell"

def main():
    #Main CLI entry point for Trebuchet modules
    arguments = docopt(__doc__, version=__version__)
    base_host = arguments['--host']
    port = int(arguments['--port'])
    protocol = arguments['--use_https'] or None
    with open(arguments['--host_list']) as hostfile:
        brute_force = hostfile.readlines()
        brute_force_list = [host.strip() for host in brute_force]
        hosts_to_investigate = enumerate_virtual_hosts(base_host, brute_force_list, port, protocol)
        print "With the brute-force list provided, we found " + str(len(hosts_to_investigate)) + " possible virtual hosts:"
        for host in hosts_to_investigate:
            print host

if __name__ == "__main__":
    main()
