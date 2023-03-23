import requests
#  Signs (Aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius, pisces)


def get_zodiac_sign():
    zodiac_sign = input("Enter your zodiac sign: ")
    return zodiac_sign


def get_day():
    day = input("Enter the horoscope day (today, tomorrow, or yesterday): ")
    return day


def your_sign():
    sign = get_zodiac_sign()
    if sign == "leo":
        print("X")
    elif sign == "Taurus":
        print("Z")
    else:
        print("E")
    return your_sign


# parameters for the HTTP request (Aztro)
params = (('sign', get_zodiac_sign()), ('day', get_day()))

response = requests.post('https://aztro.sameerkumar.website/', params=params)
# print(response.status_code)
# print(response.text)
# print(params)
# print(response.json())
json = response.json()

print("\nHoroscope for", json.get('current_date'), '\n')
print(json.get('description'), '\n')
print('Compatibility:', json.get('compatibility'))
print('Mood:', json.get('mood'))
print('Color:', json.get('color'))
print('Lucky Number:', json.get('lucky_number'))
print('Lucky Time:', json.get('lucky_time'), "\n")
