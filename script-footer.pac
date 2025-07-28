    ];

    if (shExpMatch(host, "*.ts.net")) { return "DIRECT"; }

    var newProxyTime = new Date().getTime();
    var newProxyIndex = Math.floor(Math.random() * proxyList.length);
    if (currentProxyTime == 0 || newProxyTime - currentProxyTime > proxyDurationMilliseconds) {
        currentProxyTime = newProxyTime;
        currentProxyIndex = newProxyIndex;
    }
    return proxyList[currentProxyIndex];
}
