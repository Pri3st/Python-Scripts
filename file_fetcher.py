import requests
import pyfiglet 

ascii_banner = pyfiglet.figlet_format("Pri3st's File Fetcher")
print(ascii_banner)

url = 'https://download.sysinternals.com/files/PSTools.zip'
r = requests.get(url, allow_redirects=True)
open('PSTools.zip', 'wb').write(r.content)
print ("Files successfully fetched!")