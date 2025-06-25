var currentProxyIndex = 0;
var currentProxyTime = 0;
var proxyDuration = 1000 * 60 * 5;

function FindProxyForURL(url, host) {
    var proxyList = [
