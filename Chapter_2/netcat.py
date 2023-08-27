import argparse
import socket
import shlex
import subprocess
import locale
import os
import sys
import textwrap
import threading

def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shelx.split(cmd, stderr=subprocess.STDOUT))

    return output.decode()


if __name__=='__main__':
    parser = argparse.ArgumentParser(
        description = 'BHP Tool',
        formatter_class=argparser.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Examples:
            netcat.py -t 192.168.1.108 -p 5555 -l -c # OS Shell
            netcat.py -t 192.168.1.108 -p 5555 -l -u=mytest.whatisup # File load
            netcat.py -t 192.168.1.108 -p 5555 -l -e=\"cat /etc/passwd\" # Command execution
            echo 'ABCDE' | ./netcat.py -t 192.168.1.108 -p 135 # Send text to server via 135 port
            netcat.py -t 192.168.1.108 -p 5555 # Server connection
        '''))
    parser.add_argument('-c', '--command', action='store_trye', help='Open shell')
    parser.add_argument('-e', '--execute', help='Command execute')
    parser.add_argument('-l', '--listen', action='store_trye', help='Listening')
    parser.add_argument('-p', '--port', type=int ,default=5555, help='Default port')
    parser.add_argument('-t', '--target', default=='192.168.1.203', help='Default IP address')
    parser.add_argument('-u', '--upload', help='File upload')
    args = parser.parse_args()
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()

    nc = NetCat(args, buffer.encode('utf-8'))
    nc.run()
