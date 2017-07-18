
import sys
import blescan
import datetime
import bluetooth._bluetooth as bluez

dev_id = 0

class Beacon_data():

    for word in ["Mac", "UUID", "Major", "Minor", "Tx_Power"]:
        word = ""

    toggle = 0
    time = 0
    def _Set_(self, data):
        self.Mac = data[0]
        self.UUID = data[1]
        self.Major = data[2]
        self.Minor = data[3]
        self.Tx_Power = data[4]
        self.toggle = 0

    def _Set_flag(self, inp):
        self.toggle = inp


def main():
    try:
        sock = bluez.hci_open_dev(dev_id)
        print "ble thread started"
    except:
        print "error accessing bluetooth device..."
        sys.exit(1)

    blescan.hci_le_set_scan_parameters(sock)
    blescan.hci_enable_le_scan(sock)

    f = open("uuid_list.txt", "r")
    li = [data for data in f.read().split()]
    f.close()


    while True:
        out, out1 = [], []
        returnedList = blescan.parse_events(sock, 10)
        for beacon in returnedList:
            beacon = beacon.split(",")
            if not(beacon[1] in out):
                out.append(beacon[1])
                out1.append(beacon)
        for word in out:
            if word == "5bbe004d2e8f4765b2f70a80f4a13c4c":
                if a.toggle == 0:
                    print "IN : ", word, datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                a.toggle = 1

        for word in li:
            if not(word in out) and a.toggle == 1:
                print "OUT : ", word, datetime.now().strftime("%Y/%m/%d %H:%M:%S"), 
                a.toggle = 0
            else:
                pass

if __name__=="__main__":
   data = ["60:69:fb:65:c3:57", "5bbe004d2e8f4765b2f70a80f4a13c4c", "114", "514", "-65"]
   a = Beacon_data()
   a._Set_(data)   
   main()



