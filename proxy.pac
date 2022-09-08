function FindProxyForURL(url, host) {
   if (shExpMatch(url,"*tdc.hunteron.com*")
      || shExpMatch(url,"*crm.hunteron.com*")
    ) {
       return "PROXY 47.103.223.252:8100";
    }
   return "DIRECT;";
}