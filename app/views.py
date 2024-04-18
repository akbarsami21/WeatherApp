from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

# Create your views here.
def home(request):
    if request.method=='POST':
        city=request.POST['city']
    else:
        city='Chittagong'

    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=242a3bcda8c794f760ba0b05bf2f61f4'

    #This is a dictionary containing additional parameters to send in the request
    PARAMS={'units':'metric'}  #celcius 
    API_KEY='AIzaSyCPlRfR_OSbbzJdmM-yN2s7-pIGMboNy3Y'
    SEARCH_ENGINE_ID='510e1cf282a614fb9'
    query=city + '1920x1080'
    page=1
    start=(page-1) * 10 + 1
    searchType='image'
    try:
        city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"
        data=requests.get(city_url).json()
        count=1
        search_items=data.get('items')
        image_url=search_items[1]['link']
    
        data=requests.get(url,PARAMS).json() #send request in api
        description=data['weather'][0]['description']
        icon=data['weather'][0]['icon']
        temp=data['main']['temp']

        day=datetime.date.today()
        return render(request,'home.html',{'description':description,'icon':icon,'temp':temp,'day':day,'city':city,'exp_occured':False,'image_url':image_url})
    except:
        exp_occured=True
        messages.error(request,'City not found. Please check the spelling or not available in the API.')
        day=datetime.date.today()
        return render(request,'home.html',{'description':'Clear with periodic clouds','icon':'04n','temp':13,'day':day,'city':'Kazan ','exp_occured':exp_occured})


