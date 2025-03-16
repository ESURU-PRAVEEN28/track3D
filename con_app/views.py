from django.shortcuts import render,HttpResponse
from .models import Construction
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def userinput(request):

    if request.method == "POST":

        name = request.POST.get("name")
        cq = request.POST.get("cq")
        bq = request.POST.get("bq")
        sq = request.POST.get("sq")
        iq = request.POST.get("iq")
        ec = request.POST.get("ec")

        filter_conditions = {}


        if cq:

            filter_conditions["CementQuality"] = cq

        if bq:  # Add only if not empty

            filter_conditions["BrickQuality"] = bq

        if sq:  # Add only if not empty

            filter_conditions["SandQuality"] = sq
        if iq:  # Add only if not empty

            filter_conditions["IronQuality"] = iq
        if ec:  # Add only if not empty
            filter_conditions["EnvironmentalCondition"] = ec
        if name:
            filter_conditions["ConstructionType"] = name
        data1 = Construction.objects.filter(**filter_conditions)
        return render(request, "userinput.html", {"data": data1})
    return render(request, "userinput.html")



