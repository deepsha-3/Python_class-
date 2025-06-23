import requests

name= input("Enter your name:")
city= input("Enter your city:")

api_key="c7a4931c2888b402d0c99f65dbe6c6cd"
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# response=requests.get(url)
# data=response.json()
# temp=data['main']['temp']
# description= data['weather'][0]['description']

# # print(data["main"]["temp"])


# print(f"Hello {name}!  It's currently {temp}°C with {description} in {city}.")

# # print(data)



import requests

name = input("Enter your name: ")
country = input("Enter your country: ")

url = f"https://disease.sh/v3/covid-19/countries/{country}"
response = requests.get(url)
data = response.json()

cases = data['cases']
deaths = data['deaths']
recovered = data['recovered']

print(f"Hello {name}! COVID Stats for {country}:")
print(f"Cases: {cases}")
print(f"Deaths: {deaths}")
print(f"Recovered: {recovered}")
