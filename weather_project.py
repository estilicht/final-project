import requests
import time

msg = "Welcome to the Weather program!" 
print(msg)


def by_city():
    city = input('Please Enter Your City Name: ')
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},us&appid=ce409506ab1a8a7428d531a46460c7e2&units=imperial'.format(city)
    res = requests.get(url)
    data = res.json()
    show_data(data)

    question = input('Do you want to do another search ? Type \n1 for Yes or \n2 for No: ')
    if question == '1':
        main()
    if question == '2':
        print("Good Bye!")
        exit()


def by_zip():
    zip_code = int(input('Please Enter Your Zip code: '))
    url = 'https://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&appid=ce409506ab1a8a7428d531a46460c7e2'.format(zip_code)
    res = requests.get(url)
    data = res.json()
    show_data(data)

    question = input('Do you want to do another search ? Type \n1 for Yes or \n2 for No: ')
    if question == '1':
        main()
    if question == '2':
        print("Good Bye!")
        time.sleep(2)
        exit()


def show_data(data):
    temp = data['main']['temp']
    hightemp = data['main']['temp_max']
    lowtemp = data['main']['temp_min']
    wind_speed = data['wind']['speed']
    press = data['main']['pressure']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    humid = data['main']['humidity']
    description = data['weather'][0]['description']

    print('The weather for your location is :')
    print('Current Temperature : {} degrees fahrenheit'.format(temp))
    print('High Temperature : {} degrees fahrenheit'.format(hightemp))
    print('Low Temperature : {} degrees fahrenheit'.format(lowtemp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Pressure : {} hPa'.format(press))
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    print('Humidity : {} %'.format(humid))
    print('Description : {}'.format(description))


def main():
    while True:
        answer = input("You can search the weather by zip code or city. Please type \n1 for city name or \n2 for zip code: ")
        if answer == '1':
            try:
                print("Requesting...")
                by_city()

            except Exception:
                print("Error. Invalid city")
                by_city()

        if answer == '2':
            try:
                print("Requesting...")
                by_zip()

            except Exception:
                print("Error. Invalid zip code")
                by_zip()

        else:
            print("Please choose a valid option")


main()