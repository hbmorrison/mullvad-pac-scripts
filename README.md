# Mullvad PAC Scripts

Creates a PAC script that randomises SOCKS5 proxy connections through the
Mullvad VPN / proxy network. Requires an active Mullvad VPN connection. The
PAC script is automatically updated from the Mullvad API and then filtered
to only include SOCKS5 proxies in countries covered by the
[GDPR](https://www.edpb.europa.eu/sme-data-protection-guide/faq-frequently-asked-questions/answer/what-gdpr_en)
or having GDPR-like privacy policies.

## Usage

Use the following URL to configure your browser:

- https://hbmorrison.github.io/mullvad-pac-scripts/proxy.pac

