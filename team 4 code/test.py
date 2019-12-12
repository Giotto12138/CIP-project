import subprocess

#def is_reachable(ip):
ip = "192.168.192.157"

if subprocess.call(["ping","-c","2",ip])==0:#只发送两个ECHO_REQUEST包
    print("{0} is alive.".format(ip))
else:
    print("{0} is unalive".format(ip))

