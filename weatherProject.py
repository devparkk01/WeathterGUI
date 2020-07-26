"""
author :  Dev 
"""

# importing libraries 
import tkinter as tk
from tkinter import ttk

""" Function for exiting GUI manually """
def _quit() :
    win.quit()
    win.destroy()
    exit() 


win = tk.Tk() 
win.title("Weather INFO")
win.resizable(0 , 0 )  # preventing it from being resizable 

# creating menu bar 

menuBar = tk.Menu(win )

#  adding menus to the menu items
fileMenu = tk.Menu(menuBar , tearoff= 0 )
fileMenu.add_command(label = "About")
fileMenu.add_separator()
fileMenu.add_command(label = "Exit" , command = _quit)
menuBar.add_cascade(label = "File" , menu = fileMenu)

# configuring the menubar 
win.config(menu = menuBar)


#  
"""creating a labelframe inside `win`
This will allow the user to enter the city name . """

weatherCitiesFrame = ttk.LabelFrame(win , text = "  Latest Observation for   "  )
weatherCitiesFrame.grid(row = 0 , column = 0 , padx = 8 , pady = 4 )

"""creating another labelframe inside `win`  
    Here all the weather related details will appear . 
"""

weatherConditionsFrame = ttk.LabelFrame(win , text = "  Current Weather Conditions "  )
weatherConditionsFrame.grid(row = 1 , column = 0 , padx = 2 , pady = 12 )

# adding widgets to the labelframe  `weatherCitiesFrame` we created 

ttk.Label(weatherCitiesFrame , text = "City: " ).grid(row = 0 , column = 0  )
city = tk.StringVar() # for storing the value of city

citySelected = ttk.Combobox(weatherCitiesFrame , width =24 , textvariable = city )
citySelected["values"] = ('Los Angeles, US', 'London, UK', 'Paris, FR', 'Mumbai, IN', 'Tokyo, JP' , 'Sydney, AU')
citySelected.current(0)
citySelected.grid(row = 0 , column = 1 )

#------------------------------------
# Here , This will show city and countrycode of the city selected for which the weather is displayed . 

location = tk.StringVar()
ttk.Label(weatherCitiesFrame , textvariable = location ).grid(row = 1 , column = 1 , columnspan = 2 )

#----------------------------------

#--------------------------------
# callback function to get the weather details 

def getWeather() :
    cityVar = city.get() 
    getWeatherData(cityVar)

#------------------------------------------

getWeatherbtn = ttk.Button(weatherCitiesFrame , text = "Get Weather", command = getWeather )
getWeatherbtn.grid(row = 0 , column = 2 )

# ------changing the padding of our widgets inside labelframe `weatherCitiesFrame`

for child in weatherCitiesFrame.winfo_children() :
    child.grid_configure(padx = 5, pady = 2 )

#------------------------------

ENTRY_WIDTH = 24

# Adding Label and entrybox widgets to labelFrame `weatherConditionsFrame`

ttk.Label(weatherConditionsFrame , text = "Last Updated:").grid(row = 1 , column = 0 , sticky = tk.E)
updated = tk.StringVar()
updatedEntry = ttk.Entry(weatherConditionsFrame , width = ENTRY_WIDTH , textvariable = updated , state = "readonly" , foreground = "#1F22D3" )
updatedEntry.grid(row = 1 , column = 1 ,sticky = tk.W)
#---------------------------------------------
ttk.Label(weatherConditionsFrame , text = "Weather:" ).grid(row = 2 , column = 0 , sticky = tk.E)
weather = tk.StringVar()
weatherEntry = ttk.Entry(weatherConditionsFrame , width = ENTRY_WIDTH , textvariable =weather , state = "readonly" , foreground = "#1F22D3")
weatherEntry.grid(row = 2 , column = 1 , sticky = tk.W)
#---------------------------------------------
ttk.Label(weatherConditionsFrame , text = "Temperature:").grid(row = 3 , column = 0 , sticky =tk.E)
temp = tk.StringVar()
tempEntry = ttk.Entry(weatherConditionsFrame , width = ENTRY_WIDTH , textvariable = temp , state = "readonly", foreground = "#1F22D3")
tempEntry.grid(row = 3 , column = 1 , sticky = tk.W)
#---------------------------------------------
ttk.Label(weatherConditionsFrame , text ="Relative Humidity:").grid(row = 4 , column = 0 , sticky = tk.E)
relHumidity = tk.StringVar()
relHumidityEntry = ttk.Entry(weatherConditionsFrame , width = ENTRY_WIDTH , textvariable = relHumidity , state = "readonly", foreground = "#1F22D3")
relHumidityEntry.grid(row = 4 , column = 1 , sticky = tk.W)
#---------------------------------------------
ttk.Label(weatherConditionsFrame, text="Wind:").grid( row= 5 ,column = 0 , sticky= tk.E)
wind = tk.StringVar()
windEntry = ttk.Entry(weatherConditionsFrame, width=ENTRY_WIDTH, textvariable=wind, state='readonly', foreground = "#1F22D3")
windEntry.grid( row=5, column = 1 ,  sticky=tk.W)
#---------------------------------------------
ttk.Label(weatherConditionsFrame, text="Visibility:").grid( row=6,column = 0 , sticky= tk.E)
visi = tk.StringVar()
visiEntry = ttk.Entry(weatherConditionsFrame, width=ENTRY_WIDTH, textvariable=visi, state='readonly' , foreground = "#1F22D3")
visiEntry.grid( row=6, column = 1 , sticky= tk.W)
#---------------------------------------------
ttk.Label(weatherConditionsFrame, text="Pressure:").grid( row=7,column = 0 , sticky= tk.E)
pressure = tk.StringVar()
pressureEntry = ttk.Entry(weatherConditionsFrame, width=ENTRY_WIDTH, textvariable=pressure, state='readonly' , foreground = "#1F22D3")
pressureEntry.grid( row=7, column = 1 ,  sticky= tk.W)
#---------------------------------------------
ttk.Label(weatherConditionsFrame, text="Sunrise:").grid( row=8 , column = 0 , sticky= tk.E)
sunrise = tk.StringVar()
sunriseEntry = ttk.Entry(weatherConditionsFrame, width=ENTRY_WIDTH, textvariable=sunrise, state='readonly' , foreground = "#1F22D3")
sunriseEntry.grid( row=8, column = 1 ,  sticky= tk.W)
#---------------------------------------------
ttk.Label(weatherConditionsFrame, text="Sunset:").grid( row=9, column = 0 , sticky= tk.E)
sunset = tk.StringVar()
sunsetEntry = ttk.Entry(weatherConditionsFrame, width=ENTRY_WIDTH, textvariable=sunset, state='readonly' , foreground = "#1F22D3")
sunsetEntry.grid( row=9, column = 1 ,  sticky= tk.W)
#---------------------------------------------


#------ changing the padding of our widgets inside labelframe `weatherConditionsFrame`

for child in weatherConditionsFrame.winfo_children() : 
    child.grid_configure(padx = 14 , pady = 5 )


#---------------------------------------------

"""OpenWeatherMap data collection """

from urllib.request import urlopen
import json

#------- open weather map api key 
OWM_API_KEY = 'd4d7956b1fd66c41be3ad8664f6d1c76'
#--------------
def getWeatherData(city = "London,uk") :
    city = city.replace(' ', '%20')
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, OWM_API_KEY) 
    response = urlopen(url)
    data = response.read().decode()
    jsonData = json.loads(data)

    # --------------------------------
    """
    from pprint import pprint
    pprint(jsonData) 

    This will print the fetched json data to the console 
    uncomment above lines to see how the fetched json data looks like . 

    """
    #---------------------------------

    dateTimeUnix = jsonData["dt"]     # unix timestamp 
    humidity = jsonData['main']['humidity']
    pressr = jsonData["main"]["humidity"]
    tempKelvin = jsonData['main']['temp']
    cityName = jsonData["name"]
    countryName = jsonData["sys"]["country"]
    sunriseUnix = jsonData["sys"]["sunrise"]  # unix timestamp 
    sunsetUnix = jsonData["sys"]["sunset"]   # unix timestamp 
    try :
        visibility = jsonData["visibility"]    # in case visibility is not provided in the fetched data
    except :
        visibility = 'N/A'
    
    weatherDesc = jsonData['weather'][0]['description']
    weatherIcon = jsonData['weather'][0]['icon']
    windDeg = jsonData['wind']['deg']
    windSpeed = jsonData['wind']['speed']

    def kelvinToCelsius (tempK) :
        return "{:.1f}".format(tempK - 273.15 )

    def kelvinToFahrenheit ( tempK) :
        return "{:.1f}".format((tempK - 273.15)* 1.8 + 32)

    
    from datetime import datetime
    import pytz
    # we need pytz to provide details about the timezone of the city while converting date from unixtimestamp to datetime 

    #----Helper function to convert unixtimestamp to Datetime -------------

    def unixToDatetime (unixTime) :
        return datetime.fromtimestamp(int(unixTime ), tz= pytz.FixedOffset(int(jsonData["timezone"]) / 60) ).strftime('%Y-%m-%d  %H:%M:%S')

        # jsonDate["timezone"] stores the timezone of the city ( in seconds ) .
        #  Divide it by 60 to get timezone in minutes . 
    #-------------------------------

    def meterToMiles(meter ) :
        return "{:.2f}".format((meter * 0.00062137))
    
    if ( visibility  is 'N/A') :
        visibilityMiles = "N/A"
    else :
        visibilityMiles = meterToMiles(visibility)

    
    def mpsTomph (meterSecond) :
        return "{:.1f}".format((meterSecond) * (2.23693629))

    location.set("{},{}".format(cityName , countryName))
    updated.set(unixToDatetime(dateTimeUnix))
    weather.set(weatherDesc)
    
    tempC = kelvinToCelsius(tempKelvin)
    tempF = kelvinToFahrenheit(tempKelvin)
    temp.set("{} \xb0F  ({} \xb0C )".format(tempF , tempC ) )

    relHumidity.set("{} %".format(humidity) ) 

    windSpeed = mpsTomph(windSpeed)
    wind.set("{} degrees at {} MPH".format(windDeg , windSpeed))

    visi.set("{} miles ".format(visibilityMiles))

    pressure.set("{} hPa".format(pressr))

    sunrise.set(unixToDatetime(sunriseUnix))
    sunset.set(unixToDatetime(sunsetUnix))

    #--------- To display weather icon ----------------

    import PIL.Image 
    import PIL.ImageTk

    urlIcon = "http://openweathermap.org/img/w/{}.png".format(weatherIcon)
    iconResponse = urlopen(urlIcon)
    openIm = PIL.Image.open(iconResponse )
    openPhoto = PIL.ImageTk.PhotoImage(openIm)
    imgLabel = ttk.Label(weatherCitiesFrame , image = openPhoto)
    imgLabel.image = openPhoto  # need to keep a reference of the image for images to appear,else it won't appear  . 

    imgLabel.grid(row = 1 , column = 0 )
    win.update() 

    #------------------

win.mainloop() 