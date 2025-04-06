from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


def admin_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect("/admin/")  # Redirect to Django Admin
        else:
            messages.error(request, "Invalid credentials or not an admin.")

    return render(request, "loginpage.html")


@csrf_exempt
def adddata(request):
    if request.method == "POST":
        username1 = request.POST["username"]
        password1 = request.POST["password"]
        if username1 == "admin" and password1 =="admin":
            return render(request,"recommendations/add.html")  # Redirect to Django Admin
        else:
            messages.error(request, "Invalid credentials or not an admin.")

    return render(request, "adddata.html")
