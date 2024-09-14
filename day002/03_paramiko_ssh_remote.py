import paramiko

def run_remote_command(host, username, key_file, command):
    try:
        # Create ssh client
        ssh = paramiko.SSHClient()

        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # connect to server
        ssh.connect(host, username=username, key_filename=key_file)

        # Execute the command
        stdin, stdout, stderr=ssh.exec_command(command)
        print(stdout.read().decode())
        ssh.close()
    except Exception as e:
        print(f'Error: {e}')

run_remote_command("37.27.200.203", "root", "/home/auzmor/.ssh/devops_private", "df -h")