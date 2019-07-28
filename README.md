# dnslookup
DNS lookup of a list of domains

usage: nslookup.py [-h] [-l LIST] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  
  -l LIST, --list LIST  List of dns names you want IP's for
  
  -o OUTPUT, --output OUTPUT Output file to save list
  
 # Information
 - Requires 'pip install dnspython'
 - Takes a file as input and removes newlines and http:// https://
 - Doesn't print any duplicate IP's
 - Sometimes it might print a hostname if it's in the A record
