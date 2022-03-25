import urllib.request

def get_ip():
    data = urllib.request.urlopen('https://icanhazip.com/')
    ip = data.read()
    return ip.decode()

print(get_ip())