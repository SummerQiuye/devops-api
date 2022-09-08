function FindProxyForURL(url, host) {
   if (shExpMatch(url,"**")
      || shExpMatch(url,"**")
    ) {
       return "PROXY ip";
    }
   return "DIRECT;";
}