from django.db import models
from django.contrib.auth.models import User
# Create your models here.

choice1= (('Toyota Innova Crysta Touring Sport 2.4 MT'),
       ('Toyota Etios Cross 1.4L VD'), ('Skoda Rapid 1.6 MPI AT Style'),
       ('BMW 5 Series 520d Luxury Line'), ('Skoda Rapid 1.6 MPI Ambition'),
       ('Maruti Vitara Brezza ZDi'), ('Toyota Etios Liva 1.4 VXD'),
       ('Maruti Celerio X VXI Option'),
       ('Volkswagen Ameo 1.5 TDI Comfortline'),
       ('Tata Tiago AMT 1.2 Revotron XTA'), ('Hyundai Xcent 1.2 VTVT E'),
       ('Toyota Camry Hybrid 2.5'), ('Maruti Baleno Alpha'),
       ('Honda BRV i-DTEC V MT'), ('Audi Q3 30 TDI Premium FWD'),
       ('Datsun GO T Petrol'), ('Maruti Ignis 1.2 Alpha'),
       ('Jaguar XE 2.0L Diesel Prestige'), ('Maruti Wagon R LXI'),
       ('Ford EcoSport 1.5 Diesel Titanium'),
       ('Hyundai Creta 1.6 SX Automatic'),
       ('Volkswagen Vento 1.5 TDI Highline'), ('Maruti Alto LXI'),
       ('BMW 7 Series 730Ld DPE Signature'), ('Honda Brio 1.2 S MT'),
       ('Maruti Dzire ZDI'), ('BMW 3 Series Luxury Line'),
       ('Mitsubishi Pajero Sport 4X4'), ('Hyundai Verna CRDi 1.6 AT SX Plus'),
       ('Audi Q3 35 TDI Quattro Premium Plus'), ('Toyota Etios Cross 1.2L G'),
       ('Maruti Baleno Delta CVT'), ('Hyundai Grand i10 1.2 Kappa Sportz'),
       ('Jaguar XE Portfolio'), ('Hyundai i20 Active SX Diesel'),
       ('Honda BR-V i-DTEC S MT'), ('Maruti Ignis 1.2 Delta'),
       ('Mahindra Verito 1.5 D4 BSIV'), ('Maruti Alto K10 LXI'),
       ('Toyota Innova Crysta 2.4 ZX MT'),
       ('Mahindra Verito Vibe 1.5 dCi D6'), ('Maruti Eeco 5 Seater AC'),
       ('Toyota Corolla Altis 1.8 G'), ('Hyundai Elite i20 Asta Option'),
       ('Bentley Flying Spur W12'), ('Toyota Fortuner 2.8 2WD MT'),
       ('Nissan Micra Active XV'), ('Tata Tiago 1.2 Revotron XZ'),
       ('Audi A4 35 TDI Technology'), ('Maruti Vitara Brezza LDi'),
       ('Maruti Swift VDI'), ('Hyundai Tucson 2.0 e-VGT 4WD AT GLS'),
       ('Maruti Baleno Delta'), ('Maruti Dzire AMT ZXI Plus'),
       ('Maruti Wagon R VXI AMT Opt'), ('Nissan Terrano XV D Pre'),
       ('Hyundai Verna CRDi 1.6 SX Option'), ('Nissan Micra XV CVT'),
       ('Maruti Vitara Brezza ZDi Plus Dual Tone'),
       ('Mercedes-Benz GLC 220d 4MATIC Sport'), ('Datsun GO Plus T Petrol'),
       ('Mitsubishi Pajero Sport 4X2 AT'), ('Renault KWID Climber 1.0 AMT'),
       ('Hyundai Creta 1.6 SX Diesel'), ('Mini Cooper 3 DOOR D'),
       ('Mercedes-Benz B Class B180 Sport'), ('Mahindra Bolero SLX'),
       ('Hyundai Xcent 1.2 CRDi SX'), ('BMW 5 Series 530i Sport Line'),
       ('Maruti Wagon R VXI 1.2' ), ('Renault KWID RXL'), ('Honda Jazz VX CVT'),
       ('Honda BRV i-VTEC V CVT'), ('Mahindra KUV 100 D75 K8 5Str'),
       ('Maruti Alto K10 VXI'), ('Maruti Dzire VXI'),
       ('Jeep Compass 2.0 Limited Option 4X4'),
       ('Skoda Superb L&K 2.0 TDI AT'), ('Hyundai Elantra 2.0 SX Option AT'),
       ('Hyundai Verna VTVT 1.6 SX'), ('Honda Brio 1.2 VX MT'),
       ('Mercedes-Benz GLE 250d'), ('Skoda Rapid 1.5 TDI AT Ambition'),
       ('Toyota Innova Crysta 2.8 ZX AT'), ('Skoda Superb Style 1.8 TSI AT'),
       ('Honda WRV i-DTEC VX'), ('Mercedes-Benz E-Class E 220 d'),
       ('Mahindra KUV 100 G80 K4 Plus 5Str'),
       ('Hyundai Grand i10 1.2 CRDi Magna'),
       ('Hyundai Creta 1.6 SX Automatic Diesel'),
       ('Volkswagen Vento 1.5 TDI Highline Plus AT'),
       ('Toyota Innova Crysta 2.8 GX AT 8S'), ('Maruti Ertiga VXI Petrol'),
       ('Fiat Avventura Urban Cross 1.3 Multijet Emotion'),
       ('Maruti Wagon R VXI AMT'), ('Maruti Alto K10 LXI CNG Optional'),
       ('Skoda Octavia 2.0 TDI MT Style'), ('Renault Duster 85PS Diesel RxZ'),
       ('Tata Tiago 1.2 Revotron XT Option'), ('Audi A6 35 TDI Matrix'),
       ('Jaguar XF 2.0 Petrol Portfolio'), ('Honda City i-DTEC SV'),
       ('Mercedes-Benz GLA Class 220 d 4MATIC'),
       ('Mahindra Bolero Power Plus ZLX'),
       ('Fiat Linea Classic 1.3 Multijet'), ('Audi A4 35 TDI Premium Plus'),
       ('Ford Freestyle Titanium Plus Diesel'), ('Maruti Wagon R VXI'),
       ('Renault Duster 110PS Diesel RxZ AMT'), ('Mahindra Xylo D4'),
       ('Fiat Punto EVO 1.3 Emotion'), '(Honda BR-V i-VTEC VX MT'),
       ('Volkswagen Vento 1.6 Trendline'), ('Hyundai Elantra 1.6 SX'),
       ('Datsun redi-GO T Option'), ('Mercedes-Benz SLC 43 AMG'),
       ('Mercedes-Benz GLE 350d'), ('Mahindra Bolero ZLX'),
       ('Hyundai Grand i10 1.2 CRDi Sportz'),
       ('Toyota Innova Crysta 2.4 VX MT 8S'), ('Maruti Ignis 1.2 AMT Delta'),
       ('Honda City i-VTEC CVT ZX'), ('Volkswagen Ameo 1.5 TDI Highline'),
       ('Hyundai Grand i10 1.2 Kappa Sportz AT'),
       ('Hyundai Grand i10 1.2 Kappa Magna'), ('Tata Tiago 1.2 Revotron XT'),
       ('Toyota Innova Crysta 2.8 GX AT'), ('Mahindra Thar CRDe'),
       ('Tata Zest Revotron 1.2T XE'), ('Tata Zest Quadrajet 1.3 75PS XE'),
       ('Jeep Compass 2.0 Longitude'), ('Mini Clubman Cooper S'),
       ('Maruti Vitara Brezza ZDi AMT'),
       ('Tata Tiago 1.2 Revotron XZ WO Alloy'),
       ('Hyundai Verna VTVT 1.6 AT SX Option'), ('Jeep Compass 2.0 Sport'),
       ('Maruti Vitara Brezza ZDi Plus AMT'), ('Maruti Dzire AMT VDI'),
       ('Honda City i-VTEC VX'), ('Tata Tiago 1.05 Revotorq XT Option'),
       ('Ford EcoSport 1.5 Petrol Ambiente'), ('Jeep Compass 1.4 Sport'),
       ('Hyundai Elite i20 Magna Plus'))

choise2= (('CNG'),('Petrol'),('Diesel'))

choice3= (('Manual'),('Automatic'))


choice4= (('First'),('Second'))

class prediction1(models.Model):
	Name= models.CharField(max_length= 30, choice= choice1)
	Year= models.FloatField(max_length= 5)  
	Kilometers_Driven= models.FloatField(max_length= 5)  
	Fuel_Type= models.CharField(max_length= 5, choice= choice2)  
	Transmission= models.CharField(max_length= 5, choice= choise3)        
	Owner_Type= models.CharField(max_length= 5, choice= choice4)          
	Mileage= models.FloatField(max_length= 5)              
	Engine= models.FloatField(max_length= 5)                 
	Power= models.FloatField(max_length= 5)               
	Seats= models.FloatField(max_length= 5)               
 