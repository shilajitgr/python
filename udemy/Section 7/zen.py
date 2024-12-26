from http.server import BaseHTTPRequestHandler
from io import StringIO

class HTTPRequest(BaseHTTPRequestHandler):
    def __init__(self, request_text):
        self.rfile = StringIO(request_text)
        self.raw_requestline = self.rfile.readline()
        self.error_code = self.error_message = None
        self.parse_request()

    def send_error(self, code, message):
        self.error_code = code
        self.error_message = message

    def parse_request(self): 
        self.requestline = self.raw_requestline.strip()
    
request_text = """GET / HTTP/1.1
Host: localhost:8001
Connection: keep-alive
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36
Accept-Encoding: gzip, deflate, sdch
Accept-Language: en-GB,en-US;q=0.8,en;q=0.6
"""

def f(NUMBER):
    for _ in range(NUMBER):
        HTTPRequest(request_text)

# import sys
# f(int(2500000))

import time
from urllib.request import urlopen

def download_google():
    start_time = time.time()
    r = urlopen("http://google.com")
    r.read()
    end_time = time.time()
    return end_time - start_time

def estimate_downloads_per_second():
    total_time = 0
    num_downloads = 10  # Perform 10 downloads to get an average time
    for _ in range(num_downloads):
        total_time += download_google()
    avg_time_per_download = total_time / num_downloads
    downloads_per_second = 1 / avg_time_per_download
    return downloads_per_second

downloads_per_second = estimate_downloads_per_second()
print(f"Estimated downloads per second: {downloads_per_second:.2f}")
