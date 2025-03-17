from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
from .ml_model import predict_price,add_new_data,retrain_model
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt

def recommend_material(request):
    if request.method == "POST":
        cement_quality = request.POST["cement_quality"]
        # cement_price = float(request.POST["cement_price"])
        brick_quality = request.POST["brick_quality"]
        # brick_price = float(request.POST["brick_price"])
        sand_quality = request.POST["sand_quality"]
        # sand_price = float(request.POST["sand_price"])
        iron_quality = request.POST["iron_quality"]
        # iron_price = float(request.POST["iron_price"])
        env_condition = request.POST["env_condition"]

        predicted_price = predict_price(cement_quality, brick_quality,
                                        sand_quality,  iron_quality,  env_condition)

        return render(request, "recommendations/results.html", {"predicted_price": predicted_price})

    return render(request, "recommendations/form.html")


def add(request):
    if request.method =="POST":

    # Example: Add new data
            new_data = [
                {
                    "ConstructionType": request.POST.get('name'),
                    "ConstructionName": request.POST.get('cn'),
                    "CementQuality": request.POST.get('cq'),
                    "CementPrice": request.POST.get('cp'),
                    "BrickQuality": request.POST.get('bq'),
                    "BrickPrice": request.POST.get('bp'),
                    "SandQuality": request.POST.get('sq'),
                    "SandPrice": request.POST.get('sp'),
                    "IronQuality": request.POST.get('iq'),
                    "IronPrice": request.POST.get('ip'),
                    "EnvironmentalCondition": request.POST.get('ec'),
                    "Seller": request.POST.get('s'),
                    "Price": request.POST.get('p'),
                },
                # Add more rows if needed
            ]

            add_new_data(new_data)


            retrain_model()

            return HttpResponse("new data added:")
    return render(request,'recommendations/add.html')


