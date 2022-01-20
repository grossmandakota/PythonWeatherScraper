#this program  scrapes data from weather.com and gets weather reports
#based on the zip code entered. There are comments throughout the code explaining what each thing does.

#The modules used are BeautifulSoup4 and requests. I have tested the code on 4 computers with the modules
#installed and it works on each one.


import requests
from bs4 import BeautifulSoup

#gets the temperature for today
def todayTemp(up):
    #Collects data from weather.com
    
    weather = requests.get("https://weather.com/weather/today/l/%s:4:US" % up)
    soup = BeautifulSoup(weather.text, 'html.parser')

    #Finds data from classes in HTML tags
    weather_list = soup.find(class_ = "Column--temp--5hqI_") 
    weather_list_items = weather_list.find_all('span')

    #pulls contents from HTML code
    for temp in weather_list_items:
        temps = temp.contents[0]
        print("The temperature today is: " + str(temps)+ "°\n")

#average precipitation for the month
def avgPrecipitation(up):
    avgMonth = requests.get("https://weather.com/weather/monthly/l/%s:4:US" % up)
    soup = BeautifulSoup(avgMonth.text, 'html.parser')

    month = soup.find(class_ = "historical-monthly").find('tr', class_ = "record bold-record border-record").find('td', class_ = "col-labels")
    month_list = month.find_all('span')

    avgPrecip_list = soup.find(class_ = "historical-monthly").find('tr', class_ = "record bold-record border-record").find('td', class_ = "col-precip").find('div', class_ = "dir-ltr")
    avgPrecip_list_items = avgPrecip_list.find_all('span')

    avgPrecip = avgPrecip_list_items[0].contents[0]
    return avgPrecip
 
#average high and low temps for the month   
def avgHighLow(up):
    avgMonth = requests.get("https://weather.com/weather/monthly/l/%s:4:US" % up)
    soup = BeautifulSoup(avgMonth.text, 'html.parser')

    #This is where the <span> is for average high temp of the month
    avgHigh_list = soup.find(class_ = "historical-monthly").find('tr', class_ = "record bold-record border-record").find('td', class_ = "col-high").find('div', class_ = "dir-ltr")
    avgHigh_list_items = avgHigh_list.find_all('span')
    avgLow_list = soup.find(class_ = "historical-monthly").find('tr', class_ = "record bold-record border-record").find('td', class_ = "col-low").find('div', class_ = "dir-ltr")
    avgLow_list_items = avgLow_list.find_all('span')


    #<span> for month of the year
    month = soup.find(class_ = "historical-monthly").find('tr', class_ = "record bold-record border-record").find('td', class_ = "col-labels")
    month_list = month.find_all('span')
    #Prints the high average temp of the month                                         
    for temp in avgHigh_list_items:
        for month in month_list:
            temps = temp.contents[0]
            months = month.contents[0]
            print("The average high for the month of " + str(months) + " is "  + str(temps) + "°")
    #average low temp
    for temp in avgLow_list_items:
        for month in month_list:
            temps = temp.contents[0]
            months = month.contents[0]
            print("The average low for the month of " + str(months) + " is " + str(temps) + "°\n")


#this function gets the average temperature from average high and average low. (don't touch it with a 10 foot pole)
#We had to create another function for average temp seperate from highs and lows because we needed to return it, and we had print statements in the other function            
def avgTemp(up):
    avgMonth = requests.get("https://weather.com/weather/monthly/l/%s:4:US" % up)
    soup = BeautifulSoup(avgMonth.text, 'html.parser')

    #This is where the <span> is for average temp of the month
    avgHigh_list = soup.find(class_ = "historical-monthly").find('tr', class_ = "record bold-record border-record").find('td', class_ = "col-high").find('div', class_ = "dir-ltr")
    avgHigh_list_items = avgHigh_list.find_all('span')
    avgLow_list = soup.find(class_ = "DetailsTable--value--1q_qD").find('tr', class_ = "record bold-record border-record").find('td', class_ = "col-low").find('div', class_ = "dir-ltr")
    avgLow_list_items = avgLow_list.find_all('span')
    avgHigh = avgHigh_list_items[0].contents[0]
    avgLow = avgLow_list_items[0].contents[0]
    avgTemp = (int(avgHigh) + int(avgLow)) / 2
    return avgTemp

def clothingDecisions(avgtemp, avgPrecipitation):
    print('The average temperature for the month is ' + str(avgtemp) + '°')
    if avgtemp >= 65 and avgtemp < 75:
        print('Prepare for Moderate to Warm Weather with lighter clothing.\n')
    elif avgtemp < 65 and avgtemp > 55:
        print('Prepare for Moderate to Cold temperatures with warmer clothing.\n')
    elif avgtemp > 75 and avgtemp < 85:
        print('Prepare for very warm or hot weather with very light clothing.\n')
    elif avgtemp < 55 and avgtemp > 45:
        print('Prepare for cold or chilly weather with warm clothing and possibly a jacket.\n')
    elif avgtemp > 85 and avgtemp < 95:
        print('Prepare for very hot to sweltering weather with hats, cut off clothing, and sunglasses.\n')
    elif avgtemp < 45 and avgtemp > 35:
        print('Prepare for very cold or freezing weather with heavy jackets, pants, and possibly gloves.\n')
    elif avgtemp > 95 and avgtemp < 105:
        print('You need to wear sunscreen, flipflops, a hat, and a swimsuit because the only reason it\'d be this hot is because you\'re at the beach.\n')
    elif avgtemp < 35 and avgtemp > 20:
        print('You need to prepare for human iscicle making weather and possible snow.\n')
    elif avgtemp > 105:
        print('The sun has become your enemy in this weather, dont go outside!\n')
    elif avgtemp < 20:
        print('You\'re going to experience the first half hour of Star Wars: The Empire Strikes Back in weather this cold.\n')
    
    print('The average precipitation is ' + avgPrecipitation + ' inches.')
    if eval(avgPrecipitation) >=0 and eval(avgPrecipitation) <1:
        print('The chances are very low of you encountering precipitation.')
    elif eval(avgPrecipitation) >=1 and eval(avgPrecipitation) <2:
        print('You will most likely not encounter that much precipitation.')
    elif eval(avgPrecipitation) >= 2 and eval(avgPrecipitation) <3:
        print('It is possible to encounter some precipitation so plan accordingly.')
    elif eval(avgPrecipitation) >=3 and eval(avgPrecipitation) <4:
        print('You will most likely encounter precipitation so prepare for it in combination with the temperature.')
    elif eval(avgPrecipitation) >4 and eval(avgPrecipitation) <5:
        print('You will encounter precipitation so snow, rain, and possibly sleet must be accounted for when planning your trip.')
    elif eval(avgPrecipitation) >5:
        print('Precipitation will fall in heavy amounts so maximum protection clothing might be required.')

#This note isn't important, I'm just proud that we got main down to 8 lines of code
def main():
    userPlace = input("Enter a zip code: ")
    while len(userPlace) != 5 or not userPlace.isdigit():
        print("Invalid zip code.\n")
        userPlace = input("Enter a zip code: ")
    todayTemp(userPlace)
    avgHighLow(userPlace)
    clothingDecisions(avgTemp(userPlace), avgPrecipitation(userPlace))
    
main()
