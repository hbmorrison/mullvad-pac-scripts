# Mullvad PAC Scripts

This repo maintains a PAC script that randomises SOCKS5 proxy connections
through the Mullvad VPN / proxy network.

## Notes

The PAC script is automatically updated by using the Mullvad API to fetch all
available SOCKS5 proxies. The returned proxies are then filtered to only include
those located in countries covered by the
[GDPR](https://www.edpb.europa.eu/sme-data-protection-guide/faq-frequently-asked-questions/answer/what-gdpr_en)
or having GDPR-like privacy policies, using the names listed in
[gdpr-like-countries.txt](gdpr-like-countries.txt).

In operation, the script will select a proxy at random from the list and return
that proxy when called for a period of 15 minutes. After 15 minutes, the script
will select another proxy at random from the list.

Mullvad proxies require an active Mullvad VPN connection, otherwise each request
the browser makes will face a 30 second delay waiting for the proxy connection
to time out.

If the browser is closed and re-opened, the script will be reset and select a
proxy at random when the browser makes its first request.

The script will not return a proxy for any requests to the following URL hosts:

- `*.ts.net`

This is a crude way to allow direct connections to services that are made
available over Tailscale.

## Usage

Add the following PAC script URL to your browser:

- https://hbmorrison.github.io/mullvad-pac-scripts/proxy.pac
