from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import numpy as np



# Create your views here.
def index(request):
	return render(request, 'index.html')



def signup(request):
	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		password = request.POST.get("password")
		cpassword = request.POST.get("cpassword")
		if password == cpassword:
			print("User Saved")
			user = User(
				username=name, password=password, email=email
			)
			user.save()

		return render(request, "login.html", {"name": name})
	else:
		return render(request, "signup.html")


def login(request):
	if request.method == "POST":
		email = request.POST.get("email")
		#user_obj = User.objects.get(email=email)
		password = request.POST.get("password")
		print(email,password)
		user = authenticate(username=user_obj.username, password=password)
		#user= User.objects.filter(email=email, password= password)

		if user is not None:
			auth.login(request, user)
			return redirect("prediction")
		else:
			messages.info(request, "invalid credentials")
			return redirect("login")
	else:
		return render(request, "login.html")


def about(request):
	return render(request, 'about.html')


def contactus(request):
	return render(request, 'contactus.html')


	#return render(request, 'signup.html')


def predication1(request):
	if request.method == 'POST':
		Name= request.POST['Name']
		Year= request.POST['Year']
		Kilometer_Driven= request.POST['Kilometer_Driven']
		Fuel_Type= request.POST['Fuel_Type']
		Transmission= request.POST['Transmission']
		Owner_Type= request.POST['Owner_Type']
		Mileage= request.POST['Mileage']
		Engine= request.POST.get('Engine')
		Power= request.POST['Power']
		Seats= request.POST['Seats']
		
		
		data= pd.read_csv('static/dataset/car_data.csv')

		le= LabelEncoder()
		
		name= le.fit_transform(data['Name'])
		fuel= le.fit_transform(data['Fuel_Type'])
		transmission= le.fit_transform(data['Transmission'])
		owner= le.fit_transform(data['Owner_Type'])
		
		a= data.drop(['Name', 'Fuel_Type', 'Transmission', 'Owner_Type'], axis= 1)
		a['name']= name
		a['fuel_type']= fuel
		a['transmission']= transmission
		a['owner_type']= owner

		x= a.drop(['New_Price'], axis= 1)
		y= a[['New_Price']]
		
		x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.4)

		rf= RandomForestRegressor()
		rf.fit(x_train, y_train)

		predi= np.array(
			[[
			  Name,
			  Year,
			  Kilometer_Driven,
			  Fuel_Type,
			  Transmission,
			  Owner_Type,
			  Mileage,
			  Engine,
			  Power,
			  Seats
			  ]])
		print(predi)
		pred= rf.predict(predi)
		target= pred[0]
		
		print(Name,Year,Kilometer_Driven,Fuel_Type,Transmission,Owner_Type,Mileage,Engine,Power,Seats)

		hp=predication1(
			Name,
			Year,
			Kilometer_Driven,
			Fuel_Type,
			Transmission,
			Owner_Type,
			Mileage,
			Engine,
			Power,
			Seats)
		hp.save()
		print(target)
		if target == 0:
			return render(request, 'about.html')
		else:
			return render(request, 'index.html')

	else:
		return render(request,'predication1.html')
 
		
