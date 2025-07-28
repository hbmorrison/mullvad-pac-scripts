import requests

duration_minutes = 15
duration_milliseconds = duration_minutes * 60 * 1000

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

pac_script = open('scripts/proxy.pac', 'a')

pac_script.write('var proxyDurationMilliseconds = %d;\n' % duration_milliseconds);
pac_script.write(header.read())
for item in proxy_hosts_gdpr:
    pac_script.write('        "SOCKS5 %s; DIRECT",\n' % item)
pac_script.write(footer.read())

pac_script.close()

header.close()
footer.close()
