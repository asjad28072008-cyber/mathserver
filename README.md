# Ex.05 Design a Website for Server Side Processing
# Date:01-10-2025
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
'''

<h1>serverprocess.html</h1>

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    body{
      background-color: #51f60a;
      outline:5px dotted #850ffb65;
    }
    h1{
      text-decoration:underline;
      font-size:69pt;
      text-align: center;
      background-color: rgba(123,236,255,0.98);
      color: #411edd95;

    }

    h2{
         text-decoration:underline;
         font-size: 45px;
         font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
         font-style: italic;
         font-weight: lighter;
         
    }
    #fok{
      outline:12px outset #eb0ca8d9;
      font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
      gap:23px;
      
    }

    h3{
      font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
      font-size: 78px;
      font-weight: 900;
      color:#ec0c0c87;
      text-align: center;
      text-decoration:wavy;

    }

    #but{
      background-color: #1234edac;
      font-size: 45px;
      font-weight: bolder;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;

    }
    
  </style>
</head>
<body>
   <h1>Calculator</h1>
  <form align="center" id="fok" method="POST">
  {% csrf_token %}
  <h2 > Power Of Incandescent Bulb</h2>
  <div id="it">
    <label style="font-size: 40px ;"><b>Intensity:<b></label>
    <input type="text" style="font-size: 40px; font-style:italic;" placeholder="Enter value" id="inten" name="intensity" value={{i}}>

  </div>
  <br>
  <div id="re">
    <label style="font-size: 40px;"><b>Resistance:<b></label>
      <input style="font-size: 40px; font-style:italic;" type="text" placeholder="Enter Value" id="resis" name="resistance" value={{r}}>

  </div>
  <br>
  <br>
  <br>
  <br>
  <button id="but" type="submit">Calculate</button>

  
  

  </form>
  {% if result == "Invalid input or No input was Given" %}
  <h3>Error :{{result}} </h3>
    
  {% else %}
    <h3>Power of The Bulb is :{{result}} W</h3>
  {% endif %}
</body>
</html>



```


<h1>views.py</h1>



```
from django.shortcuts import render


def power(request):
    result = None
    if request.method == "POST":
        try:
            intensity = int(request.POST.get("intensity"))
            resistance = int(request.POST.get("resistance"))
            result = (intensity ** 2) * resistance   
            print("Intensity:",intensity)
            print("Resistanve:",resistance)
            print("Power:",result)
        except:
            result = "Invalid input or No input was Given"
            print("Invalid input")

    
    return render(request,'serverprocess.html',{"result":result})


```

<h1>urls.py</h1>

```
from django.contrib import admin
from django.urls import path
from pi2r.views import power

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',power),
]

```

'''

# SERVER SIDE PROCESSING:

![alt text](<Screenshot 2025-10-01 154551.png>)


# HOMEPAGE:

![alt text](<Screenshot 2025-10-01 140525.png>)

# RESULT:
The program for performing server side processing is completed successfully.
