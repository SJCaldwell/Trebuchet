import socket
import requests
from requests import Request, Session
from requests.packages.urllib3.exceptions import InsecureRequestWarning
#Need to disable the certificate validation.
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def enumerate_virtual_hosts(base_host, list_of_subdomains, port, isHttps):
    found_hosts = set()
    protocol = "https" if isHttps else "http"
    ip = socket.gethostbyname(base_host)
    request = requests.get(protocol + "://" + ip + "/", verify = False)


    for domain in list_of_subdomains:
        s = Session()
        request = Request("GET", protocol + "://" + ip + ":" + str(port), headers={"Host": domain + "." + base_host})
        prepped = request.prepare()
        resp = s.send(prepped, verify=False, allow_redirects=False)
        if resp.status_code == 301 or resp.status_code == 302:
            found_hosts.add(resp.headers['Location'])
    return list(found_hosts)
