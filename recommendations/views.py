from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
from .ml_model import predict_price,add_new_data,retrain_model
from django.views.decorators.csrf import csrf_exempt
from con_app.models import Construction, EnvironmentalCondition, Seller
import pandas as pd
import os


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

def import_file():
    # Path to the CSV file (you can adjust this based on where your file is)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATASET_PATH = os.path.join(BASE_DIR, "construction_data.csv")

    # Read the CSV file using pandas
    df = pd.read_csv(DATASET_PATH)

    # Loop through each row in the dataframe and save it to the database
    for _, row in df.iterrows():

        rry = EnvironmentalCondition.objects.get(condition=row['EnvironmentalCondition'])
        rrys = Seller.objects.get(name=row['Seller'])

        # Create and save a new Student instance for each row
        student = Construction(
            ConstructionType=row['ConstructionType'],
            ConstructionName=row['ConstructionName'],
            CementQuality=row['CementQuality'],
            CementPrice=row['CementPrice'],
            BrickQuality=row['BrickQuality'],
            BrickPrice=row['BrickPrice'],
            SandQuality=row['SandQuality'],
            SandPrice=row['SandPrice'],
            IronQuality=row['IronQuality'],
            IronPrice=row['IronPrice'],
            EnvironmentalCondition=rry,
            Seller=rrys,
            Price=row['Price']
        )

        student.save()



def add(request):
    if request.method =="POST":
            rry = EnvironmentalCondition.objects.get(condition=request.POST.get('ec'))
            rrys = Seller.objects.get(name=request.POST.get('s'))

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
                    "EnvironmentalCondition": rry,
                    "Seller": rrys,
                    "Price": request.POST.get('p')
                },
                # Add more rows if needed
            ]

            add_new_data(new_data)


            retrain_model()
            Construction.objects.all().delete()
            import_file()



            return render(request,'recommendations/add.html')
    return render(request,'recommendations/add.html')



def environ(request):
    return HttpResponse("this is about conditions")


