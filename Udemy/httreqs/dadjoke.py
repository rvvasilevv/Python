import requests
broika=0
url='https://icanhazdadjoke.com/search'
tursena_duma=input("Napishi duma")
response=requests.get(
    url,
    headers={"Accept": "application/json"},
    params={'term':tursena_duma}
)

jsonresp=response.json()
results=jsonresp['results']
for shegi in results:
    broika+=1
    print(shegi['joke'])
print(f'Broika shegi:{broika}')
