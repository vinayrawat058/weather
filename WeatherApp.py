import tkinter as tk
from _ast import Lambda
import requests

HEIGHT = 500
WIDTH = 600

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width = WIDTH)
canvas.pack()

#e56c9986ec6c3c2f9a29b663d2035073
#api.openweathermap.org/data/2.5/forecast?q={city name},{state code}&appid={your api key}


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions:  %s \nTemperature (F):  %s' % (name,desc,temp)
    except:
        final_str = 'There was a problem retreiving that information'
    
    return final_str

def get_weather(city):
    weather_key = 'e56c9986ec6c3c2f9a29b663d2035073'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q':city, 'units':'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)

    
frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth = 0.75, relheight = 0.1,anchor='n')

entry = tk.Entry(frame,font = 40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)


lower_frame = tk.Frame(root,bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font = 40)
label.place(relwidth=1, relheight=1)



root.mainloop()
