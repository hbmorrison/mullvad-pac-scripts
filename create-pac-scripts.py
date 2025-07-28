import requests

duration_minutes = 15

proxies = requests.get('https://api.mullvad.net/www/relays/wireguard/').json()

with open('gdpr-like-countries.txt', 'r') as file:
    gdpr_countries = file.read().splitlines()

proxy_hosts_gdpr = []

for proxy in proxies:
    if proxy['active']:
        for country in gdpr_countries:
            if proxy['country_name'] == country:
                proxy_hosts_gdpr.append('%s:%s' % (proxy['socks_name'], proxy['socks_port']))
                break

header = open('script-header.pac', 'r')
footer = open('script-footer.pac', 'r')

with open('scripts/proxy.pac', 'a') as gdpr:
    gdpr.write('var proxyDurationMilliseconds = %d;\n' % duration_minutes * 60 * 1000);
    gdpr.write(header.read())
    for item in proxy_hosts_gdpr:
        gdpr.write('        "SOCKS5 %s; DIRECT",\n' % item)
    gdpr.write(footer.read())

header.close()
footer.close()
