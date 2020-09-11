#test for bash loop ping sweep
import subprocess

for ping in range(0,254):
        address = "10.11.1." + str(ping)
        res = subprocess.call(['ping', '-c', '2', address])
        if res == 0:
                print("ITS ALIVE!"), address
        elif res ++ 2:
                print("NOBODY WILL ANSWER THE DOOR! :("), address
        else:
                print("ping to", address, "failed")
