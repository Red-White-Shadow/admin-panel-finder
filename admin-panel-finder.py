#Red White Shadow Admin Panel Finder v0.1
from urllib.request import *
from urllib.error import *

print ("{0:*^54}" .format (" Red White Shadow Admin Panel Finder "))

#open links file
file = open('link.txt' , 'r')
link = input ('Enter The Website Link (www.example.com) : ')
print ('\nAvailable Links\n')
while True:
    sub_link = file.readline () .split ('\n') [0]
    
    if not sub_link:
        break

    req_link = 'http://'+link+'/'+sub_link

    try:
        response = urlopen (req_link)
    except HTTPError as e:
        continue
    except URLError as e:
        continue
    else:
        print (" [+] Ok -> ",req_link)


