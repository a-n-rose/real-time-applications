'''
Search available bluetooth devices
Print them
Select 1
Connect with bluetooth device
'''

import bluetooth


def main():
    nearby_devices = bluetooth.discover_devices()
    print("Detected devices: ")
    for i, device in enumerate(nearby_devices):
        print("{}) {}".format(i,device))
    return None
    
if __name__=="__main__":
    main()
