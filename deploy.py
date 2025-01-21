import os
import paramiko
import io

def deploy():
    # Retrieve environment variables
    ec2_host = os.getenv('EC2_HOST')
    ec2_username = os.getenv('EC2_USERNAME')
    # ec2_private_key = os.getenv('EC2_PRIVATE_KEY')  # Convert to proper format

    with open('gitlab-ci-cd.pem', 'r') as key_file:
        ec2_private_key = key_file.read()
        
    # Log the environment variables (sensitive information should be handled carefully)
    print("EC2_HOST:", ec2_host)
    print("EC2_USERNAME:", ec2_username)
    # Do not print the private key for security reasons
    print("EC2_PRIVATE_KEY: [REDACTED]",ec2_private_key)  # Redact the private key in logs


    # Create an SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Load the private key
    private_key = paramiko.RSAKey.from_private_key(io.StringIO(ec2_private_key))

    # Connect to the EC2 instance
    ssh.connect(hostname=ec2_host, username=ec2_username, pkey=private_key)

    # Commands to run on the EC2 instance
    commands = [
        "cd /var/www/http/kls360/load-board-backend-v1",  # Change to your app directory
        "git pull origin development",   # Pull the latest code
        "yarn",                          # Install dependencies
        "yarn run staging:restart"       # Restart the application using PM2
    ]

    for command in commands:
        stdin, stdout, stderr = ssh.exec_command(command)
        print(stdout.read().decode())
        print(stderr.read().decode())

    ssh.close()

if __name__ == "__main__":
    deploy()