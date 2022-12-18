import platform
import subprocess

def ping(ipAddr, timeout=100):
    '''
    Send a ping packet to the specified host, using the system ping command.
    Accepts ipAddr as string for the ping destination.
    Accepts timeout in ms for the ping timeout.
    Returns True if ping succeeds otherwise Returns False.
        Ping succeeds if it returns 0 and the output includes b'TTL='
    '''
    if platform.system().lower() == 'windows':
        numFlag = '-n'
    else:
        numFlag = '-c'
    completedPing = subprocess.run(['ping', numFlag, '1', '-w', str(timeout), ipAddr],
                                   stdout=subprocess.PIPE,    # Capture standard out
                                   stderr=subprocess.STDOUT)  # Capture standard error
    # print(completedPing.stdout)
    return (completedPing.returncode == 0) and (b'TTL=' in completedPing.stdout)

print(ping('185.8.172.56'))