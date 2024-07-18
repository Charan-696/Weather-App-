#___________________________________________________________________________________________________________________
#Imports
from configparser import ConfigParser
from tkinter import *
import requests
from tkinter import messagebox
from PIL import ImageTk,Image
#/Imports
#__________________________________________________________________________________________________________________

#Weblink
url='http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
#/Weblink

#Some Website requestites
config_file='api.ini'
config=ConfigParser()
config.read(config_file)
api_key=config['api_key']['key']
#/Some Website requesties

#Function that extracts values from web
def get_weather(city):

    result=requests.get(url.format(city,api_key))
    if result:
        json = result.json()
        city=json["name"]
        country=json["sys"]["country"]
        temp_kelvin=json["main"]["temp"]
        temp_celcius=temp_kelvin-273.15
        temp_farenheit=(temp_kelvin-273.15)*9/5+32
        icon=json["weather"][0]["icon"]
        weather=json["weather"][0]["main"]
        description=json["weather"][0]["description"]
        final=(city,country,temp_celcius,temp_farenheit,icon,weather,description)
        return final
    else:
        pass
#/Function that extracts values from web

#__________________________________________________________________________________________________________________

#Function that prints values on app interface
def search():
    city=city_text.get()
    weather=get_weather(city)
    if weather:
        location_lbl["text"]="{},{}".format(weather[0],weather[1])
        temp_lbl["text"]="{:.2f}°C,{:.2f}°F".format(weather[2],weather[3])
        weather_lbl["text"]=weather[5]
        dis_label["text"]=weather[6]
        #Weather Condition Images
        if dis_label["text"]=="clear sky":
            a["file"]="01d.png"
        elif dis_label["text"]=="few clouds":
            a["file"]="02d.png"
        elif dis_label["text"]=="Thunderstorm":
            a["file"]="11d.png"
        
        elif dis_label["text"]=="scattered clouds":
            a["file"]="03d.png"
        elif dis_label["text"]=="broken clouds":
             a["file"]="04d.png"
        elif dis_label["text"]=="shower rain":
             a["file"]="09d.png"
        elif dis_label["text"]=="rain":
             a["file"]="10d.png"
        elif dis_label["text"]=="snow":
            a["file"]="13d.png"
        elif dis_label["text"]=="mist":
             a["file"]="50d.png"

        elif weather_lbl["text"]=="Mist":
            a["file"]="50d.png"
        elif weather_lbl["text"]=="Smoke":
            a["file"]="50d.png"
        elif weather_lbl["text"]=="Haze":
            a["file"]="50d.png"
        elif weather_lbl["text"]=="Dust":
            a["file"]="50d.png"
        elif weather_lbl["text"]=="Fog":
            a["file"]="50d.png"
        elif weather_lbl["text"]=="Sand":
            a["file"]="50d.png"
        elif weather_lbl["text"]=="Dust":
            a["file"]="50d.png"
        elif weather_lbl["text"]=="Ash":
            a["file"]="50d.png"
        elif weather_lbl["text"]=="Squall":
            a["file"]="50d.png"
        elif weather_lbl["text"]=="Tornado":
            a["file"]="50d.png"
        elif weather_lbl["text"]=="Rain":
            a["file"]="10d.png"
        elif weather_lbl["text"]=="Snow":
            a["file"]="13d.png"
        elif weather_lbl["text"]=="Clouds":
            a["file"]="04d.png"
        else:
            a["file"]="10d.png"
        #/Weather Condition Images
    else:
        messagebox.showwarning("Error","Cannot find the city {} try again! ".format(city))
         
#/Function that prints values on app interface

#__________________________________________________________________________________________________________________

#App interface and geometry
app=Tk()
app.title("Weather App")
app.geometry('640x360')
app.resizable(False,False)
app.config(bg="white")
backgrounds=Canvas(app,width=360,height=640)
backgrounds.pack(fill="both",expand=True)
l_mode=Image.open("l_mode1.png")
l_mode0=l_mode.resize((640,360))
lmode=ImageTk.PhotoImage(l_mode0)
d_mode=Image.open("d_mode.png")
d_mode0=d_mode.resize((640,360))
dmode=ImageTk.PhotoImage(d_mode0)
backgrounds.create_image(0,0,image=lmode,anchor="nw")
p1=PhotoImage(file="p1.png")
app.iconphoto(False,p1)
#/App interface and geometry

#/
#Dark/Light Mode
button_mode=True

def customize():
    global button_mode
    if button_mode:
        button.config(image=off2,bg="#030201",activebackground="#030201")
        backgrounds.create_image(0,0,image=dmode,anchor="nw")
        location_lbl.config(bg="#26242f",fg="#ffa640")
        temp_lbl.config(bg="#26242f",fg="#ffa640")
        location_name_canvas=backgrounds.create_text(300,55,text="Location:",font=(str(text_font),14),fill="#ffa640")
        temp_name_canvas=backgrounds.create_text(80,300,text=" 🌡Temperature: ",font=(str(text_font),14),fill="#ffa640")
        weather_name_canvas=backgrounds.create_text(290,300,text=" Weather: ",fill="#ffa640",font=(str(text_font),14))
        dis_name_canvas=backgrounds.create_text(520,300,text="Description:",fill="#ffa640",font=(str(text_font),14))
        b.config(bg="#26242f")
        search_btn.config(bg="#26242f",fg="#ffa640")
        city_entry.config(bg="#26242f",fg="#ffa640")
        weather_lbl.config(bg="#26242f",fg="#ffa640")
        dis_label.config(bg="#26242f",fg="#ffa640")
        button_mode=False

    else:
        button.config(image=on2,bg="#dcdcdc",activebackground="#dcdcdc")
        backgrounds.create_image(0,0,image=lmode,anchor="nw")
        location_lbl.config(bg="White",fg="#26242f")
        temp_lbl.config(bg="White",fg="#26242f")
        location_name_canvas=backgrounds.create_text(300,55,text="Location:",font=(str(text_font),14),fill="#3d0b03")
        temp_name_canvas=backgrounds.create_text(80,300,text=" 🌡Temperature: ",font=(str(text_font),14),fill="#3d0b03")
        weather_name_canvas=backgrounds.create_text(290,300,text=" Weather: ",fill="#3d0b03",font=(str(text_font),14))
        dis_name_canvas=backgrounds.create_text(520,300,text="Description:",fill="#3d0b03",font=(str(text_font),14))
        b.config(bg="sky blue")
        search_btn.config(bg="White",fg="grey")
        city_entry.config(bg="White",fg="Black")
        weather_lbl.config(bg="White",fg="#3d0b03")
        dis_label.config(bg="White",fg="#3d0b03")
        button_mode=True
on=Image.open("light.png")
off=Image.open("dark.png")

on1=on.resize((100,40))
off1=off.resize((100,40))

on2=ImageTk.PhotoImage(on1)
off2=ImageTk.PhotoImage(off1)

button=Button(app,image=on2,bg="#dcdcdc",activebackground="#dcdcdc",command=customize,border=0)
button_canvas=backgrounds.create_window(480,2,window=button,anchor="nw")
#/ Dark/Light Mode
#__________________________________________________________________________________________________________________

#Font variable
text_font="Comic Sans MS"
#/Font variable

#Search bar
city_text=StringVar()
city_entry=Entry(app,textvariable=city_text,justify="center",width=18,font=(str(text_font),12),border=0,bg="White",fg="Black")
city_entry.focus()
city_entry_canvas=backgrounds.create_window(210,3,anchor="nw",window=city_entry)
#/Search bar

#Search button
search_btn=Button(app,text="🔍",bg="white",activebackground="grey",command=search,cursor="hand2",borderwidth=0)
search_btn_canvas=backgrounds.create_window(393,5,anchor="nw",window=search_btn)
app.bind("Return",lambda event:search())
app.bind("<F7>",lambda event:customize())
#/Search button

#Location Label
location_name_canvas=backgrounds.create_text(300,55,text="Location:",font=(str(text_font),14),fill="#3d0b03")
location_lbl=Label(app,text="City , Country",font=(str(text_font),14),fg="#3d0b03",bg="white")
location_lbl_canvas=backgrounds.create_window(250,65,anchor="nw",window=location_lbl)
#/Location Label

#Weather Icon Label
a=PhotoImage(file="IMAGE1.png")
b=Label(app,image=a,bg="sky blue")
b.place(x=270,y=145)
#/Weather Icon Label

#Temperature Label
temp_name_canvas=backgrounds.create_text(80,300,text=" 🌡Temperature: ",font=(str(text_font),14),fill="#3d0b03")
temp_lbl=Label(app,text="Celcius , Fahrenheit",font=(str(text_font),14),bg="white",fg="#3d0b03")
temp_lbl_canvas=backgrounds.create_window(8,315,window=temp_lbl,anchor="nw")
#/Temperature Label

#Weather condtion Label
weather_name_canvas=backgrounds.create_text(290,300,text=" Weather: ",fill="#3d0b03",font=(str(text_font),14))
weather_lbl=Label(app,text="🌤",font=(str(text_font),14),bg="white",fg="#3d0b03")
weather_lbl_canvas=backgrounds.create_window(270,315,window=weather_lbl,anchor="nw")
#/Weather condtion Label

#Description Label
dis_name_canvas=backgrounds.create_text(520,300,text="Description:",fill="#3d0b03",font=(str(text_font),14))
dis_label=Label(app,text="           💭         ",font=(str(text_font),14),bg="white",fg="#3d0b03")
dis_label_canvas=backgrounds.create_window(450,315,window=dis_label,anchor="nw")
#/Description Label

#Exception
city="Bengaluru"
try: 
    get_weather(city)
except:
    messagebox.showwarning("Network Error","Connect to internet")
app.mainloop()
#/Exception