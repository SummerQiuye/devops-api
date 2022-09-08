function FindProxyForURL(url, host) {
   if (shExpMatch(url,"*tdc.hunteron.com*")
      || shExpMatch(url,"*crm.hunteron.com*")
    ) {
       return "PROXY ip";
    }
   return "DIRECT;";
}