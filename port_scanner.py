import socket

target=input("Enter the IP Address of our Target")
portrange=input("Enter the range of the ports you want to scan in the following format 'lowest_port-highest_port'")

lowport=int(portrange.split('-')[0])
highport=int(portrange.split('-')[1])

print("Initiating port scan to target", target, "from port", lowport, "to port", highport)

for port in range(lowport, highport+1):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status=s.connect_ex((target, port))
    if(status==0):
        print("Port", port, "is open!")
    else:
        print("Port", port, "is closed")
    s.close

print("Happy hunting, hacker!")