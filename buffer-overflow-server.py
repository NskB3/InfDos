#By HiCo Adam
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 8080))
s.listen(5)
conn, addr = s.accept()
print("Connection Established")
list = []
while True:
      try:
         list.append(conn.recv(65536))
      except MemoryError:
         print("MemoryError Happened, Bypassing Shutdown...")
         list = []
