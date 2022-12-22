import requests
url='http://www.google.com'
response=requests.get(url)
print(f'Your request to {url} came back w/ status code {response.status_code}')
print(response.text)
#200-usp
#300-redirect
#400-client error
#500-server error