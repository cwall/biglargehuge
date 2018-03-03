
var browserName,browserVersion,webfontType;if(typeof(woffEnabled)=='undefined'){var woffEnabled=true;}
var svgEnabled=1;if(typeof(customPath)!='undefined'){var path=customPath;}
else
{var scripts=document.getElementsByTagName("SCRIPT");var script=scripts[scripts.length-1].src;if(!script.match("://")&&script.charAt(0)!='/')
script="./"+script;var path=script.replace(/\\/g,'/').replace(/\/[^\/]*\/?$/,'');}
var wfpath=path+"/webfonts/";var browsers=[{'regex':'MSIE (\\d+\\.\\d+)','versionRegex':'new Number(RegExp.$1)','type':[{"version":9.0,"type":"woff"},{"version":5.0,"type":"eot"}]},{'regex':'Firefox[\/\s](\\d+\\.\\d+)','versionRegex':'new Number(RegExp.$1)','type':[{"version":3.6,"type":"woff"},{"version":3.5,"type":"ttf"}]},{'regex':'Chrome\/(\\d+\\.\\d+)','versionRegex':'new Number(RegExp.$1)','type':[{"version":6.0,"type":"woff"},{"version":4.0,"type":"ttf"}]},{'regex':'Mozilla.*Android (\\d+\\.\\d+).*AppleWebKit.*Safari','versionRegex':'new Number(RegExp.$1)','type':[{"version":4.1,"type":"woff"},{"version":2.2,"type":"ttf"}]},{'regex':'Mozilla.*(iPhone|iPad).* OS (\\d+)_(\\d+).* AppleWebKit.*Safari','versionRegex':"new Number(RegExp.$2) + (new Number(RegExp.$3) / 10)","unhinted":true,'type':[{"version":4.2,"type":"ttf"},{"version":1.0,"type":"svg"}]},{'regex':'Mozilla.*(iPhone|iPad|BlackBerry).*AppleWebKit.*Safari','versionRegex':'1.0','type':[{"version":1.0,"type":"svg"}]},{'regex':'Version\/(\\d+\\.\\d+)(\\.\\d+)? Safari\/(\\d+\\.\\d+)','versionRegex':'new Number(RegExp.$1)','type':[{"version":5.1,"type":"woff"},{"version":3.1,"type":"ttf"}]},{'regex':'Opera\/(\\d+\\.\\d+)(\.+)Version\/(\\d+\\.\\d+)(\\.\\d+)?','versionRegex':'new Number(RegExp.$3)','type':[{"version":11.1,"type":"woff"},{"version":10.1,"type":"ttf"}]},]
if(/(Macintosh|Android)/.test(navigator.userAgent))
var suffix="_unhinted";else
var suffix="";var browLen=browsers.length;out:for(i=0;i<browLen;i++){var regex=new RegExp(browsers[i].regex);if(regex.test(navigator.userAgent)){browserVersion=eval(browsers[i].versionRegex);var typeLen=browsers[i].type.length;for(j=0;j<typeLen;j++){if(browserVersion>=browsers[i].type[j].version){if(browsers[i].unhinted){suffix="_unhinted";}
webfontType=browsers[i].type[j].type;if(webfontType=="woff"&&!woffEnabled){continue;}
else if(webfontType=="svg"&&!svgEnabled){continue;}
else{break out;}}}}}
var fonts=[{"fontFamily":"Nexa-Bold","url":wfpath+"25CE35_0"+suffix+"_0."+webfontType},{"fontFamily":"Nexa-Book","url":wfpath+"25CE35_1"+suffix+"_0."+webfontType},{"fontFamily":"Nexa-Light","url":wfpath+"25CE35_2"+suffix+"_0."+webfontType},{"fontFamily":"NexaBlack","url":wfpath+"25CE35_3"+suffix+"_0."+webfontType},{"fontFamily":"NexaThin","url":wfpath+"25CE35_4"+suffix+"_0."+webfontType}];var len=fonts.length;document.write("<style>");for(var i=0;i<len;i++){document.write("@font-face{font-family: "+fonts[i].fontFamily+";src:url("+fonts[i].url+");");if(fonts[i].fontWeight){document.write("font-weight: "+fonts[i].fontWeight+";");}
if(fonts[i].fontStyle){document.write("font-style: "+fonts[i].fontStyle+";");}
document.write("}");}
document.write("</style>");