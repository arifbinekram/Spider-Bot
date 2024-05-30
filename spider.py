import urllib.request
from bs4 import BeautifulSoup
import sys

urls = []
urls2 = []

# Get the target URL from command line arguments
tarurl = sys.argv[1]

# Create a request with a user-agent header
req = urllib.request.Request(tarurl, headers={'User-Agent': 'Mozilla/5.0'})
url = urllib.request.urlopen(req).read()
soup = BeautifulSoup(url, 'html.parser')

# Find all links on the page
for line in soup.find_all('a'):
    newline = line.get('href')
    try:
        if newline[:4] == "http":
            if tarurl in newline:
                urls.append(str(newline))
        elif newline[:1] == "/":
            combline = tarurl + newline
            urls.append(str(combline))
    except Exception as e:
        pass

# Process the collected URLs
for uurl in urls:
    req = urllib.request.Request(uurl, headers={'User-Agent': 'Mozilla/5.0'})
    url = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(url, 'html.parser')
    for line in soup.find_all('a'):
        newline = line.get('href')
        try:
            if newline[:4] == "http":
                if tarurl in newline:
                    urls2.append(str(newline))
            elif newline[:1] == "/":
                combline = tarurl + newline
                urls2.append(str(combline))
        except Exception as e:
            pass

# Remove duplicates
urls3 = set(urls2)

# Print the collected URLs
for value in urls3:
    print(value)

