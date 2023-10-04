import paramiko

def ssh_command(ip, port, user, passwd, cmd): 
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, usernme=user, password=passwd)

    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print('---Results---')
        for line in output:
            print(liune.strip())

    if __name=='__main__':
        import getpass
        #user = getpass.getuser()
        user = input('User name: ')
        password = getpass.getpass('Password: ')

        ip = input('Server IP address: ') or '192.168.1.203'
        port = input('Port: ') or 2222
        cmd = input('Command: ') or 'id'
        ssh_command(ip, port, user, password, cmd)
        