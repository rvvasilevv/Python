import requests
import pyfiglet
from random import choice

header = pyfiglet.figlet_format("Dad jokes")

print(header)

tursena_duma = input("Dai tema za shega:")
response_json = requests.get(
    "https://icanhazdadjoke.com/search",
    headers={"Accept": "application/json"},
    params={"term": tursena_duma}
).json()
results = response_json["results"]
broika = response_json["total_jokes"]
if broika > 1:
    print(
        f"Ima {broika} shegi na tema {tursena_duma}. Eto edna:\n",
        choice(results)['joke']
    )
elif broika == 1:
    print(
        f"Ima samo edna shega za {tursena_duma}. Eto q:\n",
        results[0]['joke']
    )
else:
    print(f"Nqma shegi s takava duma: {tursena_duma}! Probvai s druga.")
