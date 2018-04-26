import purestorage
import urllib3
import getpass
urllib3.disable_warnings()
import time

##Get array info
Array1=input("Enter FQDN or IP of the FlashArray:")
print('\n' *2)

##Get Username
uname=input("Please enter your username:")
print('\n' *2)

##Get Password (encrypted and hidden using getpass)
Password=getpass.getpass("Enter Password:")
print('\n' *2)


##Print basic array info after connection succeeds
array = purestorage.FlashArray(Array1,uname,Password)
array_info = array.get()
print ("FlashArray System ID {} , Purity Version {} ...... CONNECTION ESTABLISHED!".format(array_info['array_name'],array_info['version']))
print('\n' *2)

StatusDict=array.disable_remote_assist()
for i in StatusDict.items():
    print(i)
