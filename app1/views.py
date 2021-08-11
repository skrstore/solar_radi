from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from django.contrib import messages

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# from .models import *


# Create your views here.
def index(request):
    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")
        if password == cpassword:
            user = User.objects.create_user(
                username=name, password=password, email=email
            )
            user.save()
            print("User Saved")

            return render(request, "login.html", {"name": name})
    return render(request, "signup.html")


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user_obj = User.objects.filter(email=email)
        if user_obj.exists():
            user_obj = user_obj.first()
            user = authenticate(username=user_obj.username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("prediction")

        messages.info(request, "invalid credentials")
        return redirect("login")
    else:
        return render(request, "login.html")


def about(request):
    return render(request, "about.html")


def contactus(request):
    return render(request, "contactus.html")


def predication1(request):
    if request.method == "POST":
        Name = request.POST["Name"]
        Year = request.POST["Year"]
        Kilometer_Driven = request.POST["Kilometer_Driven"]
        Fuel_Type = request.POST["Fuel_Type"]
        Transmission = request.POST["Transmission"]
        Owner_Type = request.POST["Owner_Type"]
        Mileage = request.POST["Mileage"]
        Engine = request.POST.get("Engine")
        Power = request.POST["Power"]
        Seats = request.POST["Seats"]

        data = pd.read_csv("static/dataset/car_data.csv")

        le = LabelEncoder()

        name = le.fit_transform(data["Name"])
        fuel = le.fit_transform(data["Fuel_Type"])
        transmission = le.fit_transform(data["Transmission"])
        owner = le.fit_transform(data["Owner_Type"])

        a = data.drop(["Name", "Fuel_Type", "Transmission", "Owner_Type"], axis=1)
        a["name"] = name
        a["fuel_type"] = fuel
        a["transmission"] = transmission
        a["owner_type"] = owner

        x = a.drop(["New_Price"], axis=1)
        y = a[["New_Price"]]

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4)

        rf = RandomForestRegressor()
        rf.fit(x_train, y_train)

        predi = np.array(
            [
                [
                    Name,
                    Year,
                    Kilometer_Driven,
                    Fuel_Type,
                    Transmission,
                    Owner_Type,
                    Mileage,
                    Engine,
                    Power,
                    Seats,
                ]
            ]
        )
        print(predi)
        pred = rf.predict(predi)
        target = pred[0]

        print(
            Name,
            Year,
            Kilometer_Driven,
            Fuel_Type,
            Transmission,
            Owner_Type,
            Mileage,
            Engine,
            Power,
            Seats,
        )

        hp = predication1(
            Name,
            Year,
            Kilometer_Driven,
            Fuel_Type,
            Transmission,
            Owner_Type,
            Mileage,
            Engine,
            Power,
            Seats,
        )
        hp.save()
        print(target)
        if target == 0:
            return render(request, "about.html")
        else:
            return render(request, "index.html")

    else:
        return render(request, "predication1.html")
