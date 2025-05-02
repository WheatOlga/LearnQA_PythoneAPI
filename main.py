from json.decoder import JSONDecodeError
import requests

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)

try:
    parsed_respons_text = response.json()
    print(parsed_respons_text)
except JSONDecodeError:
    print("Response is not a JSON format")