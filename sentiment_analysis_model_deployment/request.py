import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Review':"Oh this is an awful bookA delightful awful bookJust the sort of awful bookYour whole family will adoreMy daughters requested it so often from the library, I finally just bought a copy"})

print(r.json())