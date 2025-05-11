import tkinter as tk
from tkinter import messagebox
from tkinter import *
from geopy.geocoders import Nominatim
from datetime import datetime, timedelta
import pytz
from timezonefinder import TimezoneFinder
import requests
from PIL import Image, ImageTk
import cv2

def get_weather(city):
    try:
        api_key = "bb56b6b13a5b2cbb9e5d534a6a75a2f0"
        geolocator = Nominatim(user_agent="geoapiExercises")
        geolocator.headers = {'User-Agent': 'Mozilla/5.0', 'referer': 'http://maps.google.com'}
        geolocator.api_key = 'bb56b6b13a5b2cbb9e5d534a6a75a2f0'  
        location = geolocator.geocode(city)
        if location:
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
            timezone_label.config(text=result)
            long_lat_label.config(text=f"{round(location.latitude, 4)}°N,{round(location.longitude, 4)}°E")

            home = pytz.timezone(result)
            local_time = datetime.now(home)
            current_time = local_time.strftime("%I:%M:%p")
            clock.config(text=current_time)

            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)
            data = response.json()

            if data["cod"] == 200:
                description = data["weather"][0]["description"]
                temperature = data["main"]["temp"]
                humidity = data["main"]["humidity"]
                pressure = data["main"]["pressure"]
                wind_speed = data["wind"]["speed"]

                temp_label.config(text=(temperature,"°C"))
                humidity_label.config(text=(humidity,"%"))
                pressure_label.config(text=(pressure,"hPa"))
                wind_label.config(text=(wind_speed,"m/s"))
                description_label.config(text=description)

                #first cell
                firstdayimage = data['daily'][0]['weather'][0]['icon']
                
                photo1 = ImageTk.PhotoImage(file=f"icon/{firstdayimage}@2x.png")
                firstimage.config(image=photo1)
                firstimage.image = photo1

                tempday1 =data['daily'][0]['temp']['day']
                tempnight1=data['daily'][0]['temp']['night']

                day1temp.config(text=f"Day:{tempday1}\n Night:{tempnight1}")

                #second cell
                seconddayimage = data['daily'][1]['weather'][0]['icon']

                img = Image.open(f"icon/{seconddayimage}@2x.png")
                resized_image = img.resize((50, 50))
                photo2 = ImageTk.PhotoImage(resized_image)
                secondimage.config(image=photo2)
                secondimage.image = photo2

                tempday2 = data['daily'][1]['temp']['day']
                tempnight2=data['daily'][1]['temp']['night']

                day2temp.config(text=f"Day:{tempday2}\n Night:{tempnight2}")
                               

                #third cell
                thirddayimage = data['daily'][2]['weather'][0]['icon']

                img = Image.open(f"icon/{thirddayimage}@2x.png")
                resized_image = img.resize((50, 50))
                photo3 = ImageTk.PhotoImage(resized_image)
                thirdimage.config(image=photo3)
                thirdimage.image = photo3

                tempday3 = data['daily'][2]['temp']['day']
                tempnight3=data['daily'][2]['temp']['night']

                day3temp.config(text=f"Day:{tempday3}\n Night:{tempnight3}")

                

                #fourth cell
                fourthdayimage = data['daily'][3]['weather'][0]['icon']

                img = Image.open(f"icon/{fourthdayimage}@2x.png")
                resized_image = img.resize((50, 50))
                photo4 = ImageTk.PhotoImage(resized_image)
                fourthimage.config(image=photo4)
                fourthimage.image = photo4

                tempday4 = data['daily'][3]['temp']['day']
                tempnight4=data['daily'][3]['temp']['night']

                day4temp.config(text=f"Day:{tempday4}\n Night:{tempnight4}")
               
                #fifth cell
                fifthdayimage = data['daily'][4]['weather'][0]['icon']

                img = Image.open(f"icon/{fifthdayimage}@2x.png")
                resized_image = img.resize((50, 50))
                photo5 = ImageTk.PhotoImage(resized_image)
                fifthimage.config(image=photo5)
                fifthimage.image = photo5

                tempday5 = data['daily'][4]['temp']['day']
                tempnight5=data['daily'][4]['temp']['night']

                day5temp.config(text=f"Day:{tempday5}\n Night:{tempnight5}")

                

                #sixth cell
                sixthdayimage = data['daily'][5]['weather'][0]['icon']

                img = Image.open(f"icon/{sixthdayimage}@2x.png")
                resized_image = img.resize((50, 50))
                photo6 = ImageTk.PhotoImage(resized_image)
                sixthimage.config(image=photo6)
                sixthimage.image = photo6

                tempday6 = data['daily'][5]['temp']['day']
                tempnight6=data['daily'][5]['temp']['night']

                day6temp.config(text=f"Day:{tempday6}\n Night:{tempnight6}")
                
                #seventh cell
                seventhdayimage = data['daily'][6]['weather'][0]['icon']

                img = Image.open(f"icon{seventhdayimage}@2x.png")
                resized_image = img.resize((50, 50))
                photo7 = ImageTk.PhotoImage(resized_image)
                seventhimage.config(image=photo7)
                seventhimage.image = photo7

                tempday7 = data['daily'][6]['temp']['day']
                tempnight7=data['daily'][6]['temp']['night']

                day7temp.config(text=f"Day:{tempday7}\n Night:{tempnight7}")
                

                #days

                first = datetime.now()
                day1_label.config(text=first.strftime("%A"))

                second = first + timedelta(days=1)
                day2_label.config(text=second.strftime("%A"))

                third = second + timedelta(days=1)
                day3_label.config(text=third.strftime("%A"))

                fourth = third + timedelta(days=1)
                day4_label.config(text=fourth.strftime("%A"))

                fifth = fourth + timedelta(days=1)
                day5_label.config(text=fifth.strftime("%A"))

                sixth = fifth + timedelta(days=1)
                day6_label.config(text=sixth.strftime("%A"))

                seventh = sixth + timedelta(days=1)
                day7_label.config(text=seventh.strftime("%A"))

        else:
            messagebox.showerror("Error", "City not found or API key invalid.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def search_weather():
    city = textfield.get()
    if city:
        get_weather(city)
    else:
        messagebox.showerror("Error", "Please enter a city name.")

# Create main window
root = Tk()
root.title("Weather APP")

root.geometry("890x820+200+100")
root.resizable(False,True)
weather_info = tk.Label(root, text="")

# Create a label to display the video
video_label = tk.Label(root)
video_label.pack(fill=tk.BOTH, expand=True)

# Open the video file
cap = cv2.VideoCapture("Earth globe.mp4")  

def update_video():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = Image.fromarray(frame)
        frame = ImageTk.PhotoImage(frame)
        video_label.configure(image=frame)
        video_label.image = frame
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Reset video to the beginning for looping
    root.after(10, update_video)

# Update the video in the label
update_video()

##icon
image_icon = PhotoImage(file="Images/logo.png")
root.iconphoto(False, image_icon)

Round_box = PhotoImage(file="Images/Rounded Rectangle 1.png")
Label(root, image=Round_box, ).place(x=40, y=410)

#label
label1 = Label(root, text="Temperature", font=('Helvetica', 11), fg="White", bg="#203243")
label1.place(x=50, y=420)

label2 = Label(root, text="Humidity", font=('Helvetica', 11), fg="White", bg="#203243")
label2.place(x=50, y=440)

label3 = Label(root, text="Pressure", font=('Helvetica', 11), fg="White", bg="#203243")
label3.place(x=50, y=460)

label4 = Label(root, text="Wind Speed", font=('Helvetica', 11), fg="White", bg="#203243")
label4.place(x=50, y=480)

label5 = Label(root, text="Description", font=('Helvetica', 11), fg="White", bg="#203243")
label5.place(x=50, y=500)

##search Box
Search_image = PhotoImage(file="Images/Rounded Rectangle 3.png")
myimage = Label(image=Search_image, bg="white")
myimage.place(x=250, y=420)

weat_image = PhotoImage(file="Images/Layer 7.png")
weatherimage = Label(root, image=weat_image, bg="#203243")
weatherimage.place(x=260, y=427)

textfield = tk.Entry(root, justify='center', width=15, font=('poppins', 25, 'bold'), bg="#203243", border=0, fg="White")
textfield.place(x=350, y=430)
textfield.focus()

Search_icon = PhotoImage(file="Images/Layer 6.png")
search_button = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#203243", command=search_weather)
search_button.place(x=595, y=425)

##Bottom box
frame = Frame(root, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)

#bottom boxes
firstbox = PhotoImage(file="Images/Rounded Rectangle 2.png")
secondbox = PhotoImage(file="Images/Rounded Rectangle 2 copy.png")
Label(frame, image=firstbox, bg="#212120").place(x=30, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=300, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=400, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=500, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=600, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=700, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=800, y=30)

##clock (here we will place the time)
clock = Label(root, font=("Helvetica", 30, 'bold'), fg="White", bg="#57adff")
clock.place(x=30, y=20)

#timezone
timezone_label = Label(root, font=("Helvetica", 20), fg="White", bg="#57adff")
timezone_label.place(x=700, y=20)

long_lat_label = Label(root, font=("Helvetica", 10), fg="White", bg="#57adff")
long_lat_label.place(x=700, y=50)

#thpwd
temp_label = Label(root, font=("Helvetica", 11), fg="White", bg="#203243")
temp_label.place(x=150, y=420)
humidity_label = Label(root, font=("Helvetica", 11), fg="White", bg="#203243")
humidity_label.place(x=150, y=440)
pressure_label = Label(root, font=("Helvetica", 11), fg="White", bg="#203243")
pressure_label.place(x=150, y=460)
wind_label = Label(root, font=("Helvetica", 11), fg="White", bg="#203243")
wind_label.place(x=150, y=480)
description_label = Label(root, font=("Helvetica", 11), fg="White", bg="#203243")
description_label.place(x=150, y=500)

#first cell
firstframe = Frame(root, width=230, height=132, bg="#282829")
firstframe.place(x=35, y=615)

day1_label = Label(firstframe, font="arial 20", bg="#282829", fg="#fff")
day1_label.place(x=10, y=5)

firstimage = Label(firstframe,bg="#282829")
firstimage.place(x=1,y=15)

day1temp = Label(firstframe,bg="#282829", fg="#57adff", font="arial 15 bold")
day1temp.place(x=100, y=50)

#second cell
secondframe = Frame(root, width=80, height=112, bg="#282829")
secondframe.place(x=305, y=626)

day2_label = Label(secondframe, bg="#282829", fg="#fff")
day2_label.place(x=10, y=5)

secondimage = Label(secondframe,bg="#282829")
secondimage.place(x=7,y=20)

day2temp = Label(secondframe,bg="#282829", fg="#57adff", font="arial 15 bold")
day2temp.place(x=2, y=70)

#third cell
thirdframe = Frame(root, width=80, height=112, bg="#282829")
thirdframe.place(x=405, y=626)

day3_label = Label(thirdframe, bg="#282829", fg="#fff")
day3_label.place(x=10, y=5)

thirdimage = Label(thirdframe,bg="#282829")
thirdimage.place(x=7,y=20)

day3temp = Label(thirdframe,bg="#282829", fg="#57adff", font="arial 15 bold")
day3temp.place(x=2, y=70)

#fourth cell
fourthframe = Frame(root, width=80, height=112, bg="#282829")
fourthframe.place(x=505, y=626)

day4_label = Label(fourthframe, bg="#282829", fg="#fff")
day4_label.place(x=10, y=5)

fourthimage = Label(fourthframe,bg="#282829")
fourthimage.place(x=7,y=20)

day4temp = Label(fourthframe,bg="#282829", fg="#57adff", font="arial 15 bold")
day4temp.place(x=2, y=70)

#fifth cell
fifthframe = Frame(root, width=80, height=112, bg="#282829")
fifthframe.place(x=605, y=626)

day5_label = Label(fifthframe, bg="#282829", fg="#fff")
day5_label.place(x=10, y=5)

fifthimage = Label(fifthframe,bg="#282829")
fifthimage.place(x=7,y=20)

day5temp = Label(fifthframe,bg="#282829", fg="#57adff", font="arial 15 bold")
day5temp.place(x=2, y=70)

#sixth cell
sixthframe = Frame(root, width=80, height=112, bg="#282829")
sixthframe.place(x=705, y=626)

day6_label = Label(sixthframe, bg="#282829", fg="#fff")
day6_label.place(x=10, y=5)

sixthimage = Label(sixthframe,bg="#282829")
sixthimage.place(x=7,y=20)

day6temp = Label(sixthframe,bg="#282829", fg="#57adff", font="arial 15 bold")
day6temp.place(x=2, y=70)

#seventh cell
seventhframe = Frame(root, width=80, height=112, bg="#282829")
seventhframe.place(x=805, y=626)

day7_label = Label(seventhframe, bg="#282829", fg="#fff")
day7_label.place(x=10, y=5)

seventhimage = Label(seventhframe,bg="#282829")
seventhimage.place(x=7,y=20)

day7temp = Label(seventhframe,bg="#282829", fg="#57adff", font="arial 15 bold")
day7temp.place(x=2, y=70)

root.mainloop()
