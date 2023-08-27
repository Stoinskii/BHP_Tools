import socket

target_host = 'www.example.com'
target_port = 80

# Socket object creation
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to the server
client.connect((target_host, target_port))

# Sending data
client.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
# Adding the prefix "b" to a string converts it to bytes 

# Receiving data
respone = client.recv(4096)

print(respone.decode())
client.close()