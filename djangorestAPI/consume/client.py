import requests

endpoint = "http://httpbin.org/anything"
response = requests.get(endpoint)
print(response.text)

#HTTP Resqest ---> HTML
#REST API HTTP Request ---> JSON (javascript object notation ~= python dic) 

{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8", 
    "Accept-Encoding": "gzip, deflate, br", 
    "Accept-Language": "fr-FR,fr", 
    "Host": "httpbin.org", 
    "Sec-Fetch-Dest": "document", 
    "Sec-Fetch-Mode": "navigate", 
    "Sec-Fetch-Site": "none", 
    "Sec-Fetch-User": "?1", 
    "Sec-Gpc": "1", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-635564dc-3ae3cea412721530256d03cb"
  }, 
  "json": null, 
  "method": "GET", 
  "origin": "41.202.207.146", 
  "url": "https://httpbin.org/anything"
}