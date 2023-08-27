import socket

target_host = '127.0.0.1'
target_port = 9997

# Socket object creation
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Sending the data
client.sendto(b"AAABBBCCC", (target_host, target_port))
# Adding the prefix "b" to a string converts it to bytes

# Receiving the data
data, addr = client.recvfrom(4096)

print(data.decode())
print(addr)

client.close()