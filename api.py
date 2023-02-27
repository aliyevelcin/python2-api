import requests
 

# salam = input()
# pre_result = requests.get(f'https://dog.ceo/api/breed/{salam}/images/random')
# result = pre_result.json()
# print(f'adi: {result["message"]}')
# print(f'adi: {result["status"]}')




import requests

pre_result = requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m')

result = pre_result.json()

print(f'Temperatur: {result["current_weather"]["temperature"]}')
print(f'Kulek sureti: {result["current_weather"]["windspeed"]}')
print(f'Kulek istiqameti: {result["current_weather"]["winddirection"]}')
print(f'Saat: {result["current_weather"]["time"]}')
 


