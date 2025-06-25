import requests

proxies = requests.get('https://api.mullvad.net/www/relays/wireguard/').json()

proxies_all = []
proxies_europe = []

for proxy in proxies:
    if proxy['socks_name'] is not None and proxy['active']:

        proxies_all.append(proxy['socks_name'])

        match proxy['country']:
            case 'Germany': proxies_europe.append(proxy['socks_name'])

start = open('pac-script-start.js', 'r')
finish = open('pac-script-finish.js', 'r')

with open('repo/FindProxyForURL.js', 'a') as all:
    all.write(start.read())
    for item in proxies_all:
        all.write("        \"SOCKS5 %s:1080\",\n" % item)
    all.write(finish.read())

start.seek(0)
finish.seek(0)

with open('repo/FindProxyForURL-europe.js', 'a') as europe:
    europe.write(start.read())
    for item in proxies_europe:
        europe.write("%s\n" % item)
    europe.write(finish.read())

start.close()
finish.close()
