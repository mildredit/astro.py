import requests
#  Signs (Aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius, capricorn, aquarius, pisces)

# sign = ("Aries", "taurus")


class Astrogame:
    url = 'https://aztro.sameerkumar.website/'
    valid_signs = ("aries", "taurus", "gemini", "cancer", "leo", "virgo",
                   "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces")
    sign = ""
    day = ""

    def get_zodiac_sign(self):
        zodiac_sign = input("Enter your zodiac sign: ")
        self.sign = zodiac_sign
        return zodiac_sign

    def get_day(self) -> str:
        day = input("Enter the horoscope day (today, tomorrow, or yesterday): ")
        self.day = day
        return day

    def your_sign(self, sign):
        if sign.lower() in self.valid_signs:
            print("\nThe reading for", sign, "is: ")
        else:
            print("No data available")
        return sign

    def is_valid_sign(self, sign) -> bool:
        """returns true if sign is valid, false if not"""
        return sign in self.valid_signs

    def request_astro_info(self):
        """Given a day and sign, make request to get data from astro api"""
        params = (('sign', self.sign), ('day', self.day))
        response = requests.post(self.url, params=params)
        return response.json()

    def print_reading(self, response_json):
        """print reading from the api call"""
        print("\nHoroscope for", response_json.get('current_date'), '\n')
        print(response_json.get('description'), '\n')
        print('Compatibility:', response_json.get('compatibility'))
        print('Mood:', response_json.get('mood'))
        print('Color:', response_json.get('color'))
        print('Lucky Number:', response_json.get('lucky_number'))
        print('Lucky Time:', response_json.get('lucky_time'), "\n")


astro = Astrogame()
astro.get_day()
astro.get_zodiac_sign()
astro.your_sign(astro.sign)
if astro.is_valid_sign(astro.sign):
    # astro.your_sign(astro.sign)
    response = astro.request_astro_info()
    astro.print_reading(response)


# sign = astro.get_zodiac_sign()
# day = astro.get_day()
# astro.your_sign(sign)

# if astro.is_valid_sign(sign):
    # parameters for the HTTP request (Aztro)
    # params = (('sign', sign), ('day', day))

    # response = requests.post(
    #     'https://aztro.sameerkumar.website/', params=params)
    # print(response.status_code)
    # print(response.text)
    # print(params)
    # print(response.json())
    # json = response.json()

    # print("\nHoroscope for", json.get('current_date'), '\n')
    # print(json.get('description'), '\n')
    # print('Compatibility:', json.get('compatibility'))
    # print('Mood:', json.get('mood'))
    # print('Color:', json.get('color'))
    # print('Lucky Number:', json.get('lucky_number'))
    # print('Lucky Time:', json.get('lucky_time'), "\n")
