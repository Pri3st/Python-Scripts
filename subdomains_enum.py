import requests 
import sys
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Pri3st's Subdomain Fuzzer")
print(ascii_banner) 

sub_list = open("subdomains.txt").read() 
subdoms = sub_list.splitlines()

for sub in subdoms:
    sub_domains = f"http://{sub}.{sys.argv[1]}" 

    try:
        requests.get(sub_domains)
    
    except requests.ConnectionError: 
        pass
    
    else:
        print("Valid domain: ",sub_domains)