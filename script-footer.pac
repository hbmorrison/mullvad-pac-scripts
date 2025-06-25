    ];
    var newProxyTime = new Date().getTime();
    var newProxyIndex = Math.floor(Math.random() * proxyList.length);
    if (currentProxyTime == 0 || newProxyTime - currentProxyTime > proxyDuration) {
        currentProxyTime = newProxyTime;
        currentProxyIndex = newProxyIndex;
    }
    return proxyList[currentProxyIndex];
}
