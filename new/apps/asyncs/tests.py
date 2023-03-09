import requests

url = "https://radio-world-75-000-worldwide-fm-radio-stations.p.rapidapi.com/api.php"

querystring = {"id":"15","count":"10","page":"1","category_detail":""}

headers = {
	"X-RapidAPI-Key": "b74a30d0e6mshccdcd438b0d01d6p1bdeabjsnf9b3698e390e",
	"X-RapidAPI-Host": "radio-world-75-000-worldwide-fm-radio-stations.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)