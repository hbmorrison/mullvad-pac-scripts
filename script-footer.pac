    ];
    if (shExpMatch(url, "*.ts.net")) {
        return "DIRECT";
    }
    if (shExpMatch(url, "*.home")) {
        return "DIRECT";
    }
    if (shExpMatch(url, "*.lan")) {
        return "DIRECT";
    }
    var newProxyTime = new Date().getTime();
    var newProxyIndex = Math.floor(Math.random() * proxyList.length);
    if (currentProxyTime == 0 || newProxyTime - currentProxyTime > proxyDurationMilliseconds) {
        currentProxyTime = newProxyTime;
        currentProxyIndex = newProxyIndex;
    }
    return proxyList[currentProxyIndex];
}
