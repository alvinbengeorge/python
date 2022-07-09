import urllib.request

req = urllib.request.Request('https://www.google.com')

print(urllib.request.urlopen(req))

