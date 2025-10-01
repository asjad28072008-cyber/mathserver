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
    