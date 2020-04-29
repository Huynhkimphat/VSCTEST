# regex

import re

text = "random string  Myname123@gmail.com .some more random text. YourName.8_8_8@company.net"
# match with the first appear
pattern1 = re.compile("A random string")

pattern2 = re.compile("[crd]")

pattern3 = re.compile("[a-zA-Z]")

pattern = re.compile("[a-zA-Z0-9]+")
# \. to find out dot character
pattern4 = re.compile("[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9]+\.+[a-zA-Z0-9]+")

result = pattern.search(text)
result1 = pattern4.findall(text)
print(result1)
