# Generated by Django 3.2.6 on 2021-08-13 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20210811_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredictionData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(choices=[('Toyota Camry Hybrid 2.5', 'Toyota Camry Hybrid 2.5'), ('Ford EcoSport 1.5 Diesel Titanium', 'Ford EcoSport 1.5 Diesel Titanium'), ('Toyota Innova Crysta 2.8 ZX AT', 'Toyota Innova Crysta 2.8 ZX AT'), ('Fiat Avventura Urban Cross 1.3 Multijet Emotion', 'Fiat Avventura Urban Cross 1.3 Multijet Emotion'), ('Mahindra Bolero ZLX', 'Mahindra Bolero ZLX'), ('Jeep Compass 2.0 Limited Option 4X4', 'Jeep Compass 2.0 Limited Option 4X4'), ('Mercedes-Benz E-Class E 220 d', 'Mercedes-Benz E-Class E 220 d'), ('Maruti Wagon R LXI', 'Maruti Wagon R LXI'), ('Mahindra KUV 100 D75 K8 5Str', 'Mahindra KUV 100 D75 K8 5Str'), ('Skoda Octavia 2.0 TDI MT Style', 'Skoda Octavia 2.0 TDI MT Style'), ('Maruti Vitara Brezza ZDi AMT', 'Maruti Vitara Brezza ZDi AMT'), ('Renault Duster 85PS Diesel RxZ', 'Renault Duster 85PS Diesel RxZ'), ('Maruti Ignis 1.2 Alpha', 'Maruti Ignis 1.2 Alpha'), ('Jaguar XE Portfolio', 'Jaguar XE Portfolio'), ('Maruti Vitara Brezza ZDi Plus AMT', 'Maruti Vitara Brezza ZDi Plus AMT'), ('Jaguar XF 2.0 Petrol Portfolio', 'Jaguar XF 2.0 Petrol Portfolio'), ('Datsun GO T Petrol', 'Datsun GO T Petrol'), ('BMW 3 Series Luxury Line', 'BMW 3 Series Luxury Line'), ('Mahindra KUV 100 G80 K4 Plus 5Str', 'Mahindra KUV 100 G80 K4 Plus 5Str'), ('Hyundai Verna VTVT 1.6 AT SX Option', 'Hyundai Verna VTVT 1.6 AT SX Option'), ('Honda City i-VTEC CVT ZX', 'Honda City i-VTEC CVT ZX'), ('Skoda Superb Style 1.8 TSI AT', 'Skoda Superb Style 1.8 TSI AT'), ('Hyundai Grand i10 1.2 Kappa Sportz AT', 'Hyundai Grand i10 1.2 Kappa Sportz AT'), ('Hyundai Elantra 2.0 SX Option AT', 'Hyundai Elantra 2.0 SX Option AT'), ('Toyota Innova Crysta 2.4 VX MT 8S', 'Toyota Innova Crysta 2.4 VX MT 8S'), ('Nissan Terrano XV D Pre', 'Nissan Terrano XV D Pre'), ('Mitsubishi Pajero Sport 4X2 AT', 'Mitsubishi Pajero Sport 4X2 AT'), ('Maruti Alto K10 LXI', 'Maruti Alto K10 LXI'), ('Toyota Innova Crysta 2.4 ZX MT', 'Toyota Innova Crysta 2.4 ZX MT'), ('Toyota Fortuner 2.8 2WD MT', 'Toyota Fortuner 2.8 2WD MT'), ('Maruti Wagon R VXI AMT Opt', 'Maruti Wagon R VXI AMT Opt'), ('BMW 5 Series 520d Luxury Line', 'BMW 5 Series 520d Luxury Line'), ('Renault KWID RXL', 'Renault KWID RXL'), ('Maruti Eeco 5 Seater AC', 'Maruti Eeco 5 Seater AC'), ('Toyota Etios Cross 1.4L VD', 'Toyota Etios Cross 1.4L VD'), ('Audi A6 35 TDI Matrix', 'Audi A6 35 TDI Matrix'), ('Mercedes-Benz GLA Class 220 d 4MATIC', 'Mercedes-Benz GLA Class 220 d 4MATIC'), ('Hyundai Creta 1.6 SX Automatic', 'Hyundai Creta 1.6 SX Automatic'), ('Hyundai Xcent 1.2 VTVT E', 'Hyundai Xcent 1.2 VTVT E'), ('Skoda Superb L&K 2.0 TDI AT', 'Skoda Superb L&K 2.0 TDI AT'), ('Fiat Punto EVO 1.3 Emotion', 'Fiat Punto EVO 1.3 Emotion'), ('Mitsubishi Pajero Sport 4X4', 'Mitsubishi Pajero Sport 4X4'), ('Maruti Dzire VXI', 'Maruti Dzire VXI'), ('Maruti Baleno Alpha', 'Maruti Baleno Alpha'), ('Mercedes-Benz GLE 350d', 'Mercedes-Benz GLE 350d'), ('Tata Zest Quadrajet 1.3 75PS XE', 'Tata Zest Quadrajet 1.3 75PS XE'), ('Mercedes-Benz SLC 43 AMG', 'Mercedes-Benz SLC 43 AMG'), ('Maruti Wagon R VXI 1.2', 'Maruti Wagon R VXI 1.2'), ('Honda BRV i-VTEC V CVT', 'Honda BRV i-VTEC V CVT'), ('Audi Q3 35 TDI Quattro Premium Plus', 'Audi Q3 35 TDI Quattro Premium Plus'), ('Renault Duster 110PS Diesel RxZ AMT', 'Renault Duster 110PS Diesel RxZ AMT'), ('Mahindra Xylo D4', 'Mahindra Xylo D4'), ('Honda BR-V i-VTEC VX MT', 'Honda BR-V i-VTEC VX MT'), ('Honda City i-VTEC VX', 'Honda City i-VTEC VX'), ('Mahindra Verito 1.5 D4 BSIV', 'Mahindra Verito 1.5 D4 BSIV'), ('Audi A4 35 TDI Premium Plus', 'Audi A4 35 TDI Premium Plus'), ('Maruti Vitara Brezza ZDi Plus Dual Tone', 'Maruti Vitara Brezza ZDi Plus Dual Tone'), ('Hyundai Grand i10 1.2 CRDi Sportz', 'Hyundai Grand i10 1.2 CRDi Sportz'), ('Mahindra Bolero Power Plus ZLX', 'Mahindra Bolero Power Plus ZLX'), ('Hyundai Elantra 1.6 SX', 'Hyundai Elantra 1.6 SX'), ('Honda BR-V i-DTEC S MT', 'Honda BR-V i-DTEC S MT'), ('Toyota Corolla Altis 1.8 G', 'Toyota Corolla Altis 1.8 G'), ('Hyundai Verna VTVT 1.6 SX', 'Hyundai Verna VTVT 1.6 SX'), ('Hyundai Creta 1.6 SX Automatic Diesel', 'Hyundai Creta 1.6 SX Automatic Diesel'), ('Volkswagen Vento 1.6 Trendline', 'Volkswagen Vento 1.6 Trendline'), ('Maruti Ignis 1.2 AMT Delta', 'Maruti Ignis 1.2 AMT Delta'), ('Ford EcoSport 1.5 Petrol Ambiente', 'Ford EcoSport 1.5 Petrol Ambiente'), ('Maruti Ignis 1.2 Delta', 'Maruti Ignis 1.2 Delta'), ('Maruti Vitara Brezza ZDi', 'Maruti Vitara Brezza ZDi'), ('Tata Tiago AMT 1.2 Revotron XTA', 'Tata Tiago AMT 1.2 Revotron XTA'), ('BMW 7 Series 730Ld DPE Signature', 'BMW 7 Series 730Ld DPE Signature'), ('Mahindra Verito Vibe 1.5 dCi D6', 'Mahindra Verito Vibe 1.5 dCi D6'), ('Maruti Ertiga VXI Petrol', 'Maruti Ertiga VXI Petrol'), ('Datsun redi-GO T Option', 'Datsun redi-GO T Option'), ('Mercedes-Benz B Class B180 Sport', 'Mercedes-Benz B Class B180 Sport'), ('Mahindra Thar CRDe', 'Mahindra Thar CRDe'), ('Maruti Swift VDI', 'Maruti Swift VDI'), ('Volkswagen Ameo 1.5 TDI Comfortline', 'Volkswagen Ameo 1.5 TDI Comfortline'), ('Audi A4 35 TDI Technology', 'Audi A4 35 TDI Technology'), ('Maruti Dzire AMT VDI', 'Maruti Dzire AMT VDI'), ('Toyota Innova Crysta Touring Sport 2.4 MT', 'Toyota Innova Crysta Touring Sport 2.4 MT'), ('Hyundai Grand i10 1.2 Kappa Magna', 'Hyundai Grand i10 1.2 Kappa Magna'), ('Hyundai Elite i20 Magna Plus', 'Hyundai Elite i20 Magna Plus'), ('Datsun GO Plus T Petrol', 'Datsun GO Plus T Petrol'), ('Hyundai Elite i20 Asta Option', 'Hyundai Elite i20 Asta Option'), ('Maruti Baleno Delta', 'Maruti Baleno Delta'), ('Hyundai Grand i10 1.2 Kappa Sportz', 'Hyundai Grand i10 1.2 Kappa Sportz'), ('Honda City i-DTEC SV', 'Honda City i-DTEC SV'), ('Maruti Alto K10 VXI', 'Maruti Alto K10 VXI'), ('Honda Brio 1.2 VX MT', 'Honda Brio 1.2 VX MT'), ('Mahindra Bolero SLX', 'Mahindra Bolero SLX'), ('Tata Tiago 1.2 Revotron XZ', 'Tata Tiago 1.2 Revotron XZ'), ('Maruti Wagon R VXI AMT', 'Maruti Wagon R VXI AMT'), ('Fiat Linea Classic 1.3 Multijet', 'Fiat Linea Classic 1.3 Multijet'), ('Tata Tiago 1.2 Revotron XT', 'Tata Tiago 1.2 Revotron XT'), ('Tata Tiago 1.05 Revotorq XT Option', 'Tata Tiago 1.05 Revotorq XT Option'), ('Honda BRV i-DTEC V MT', 'Honda BRV i-DTEC V MT'), ('Maruti Dzire AMT ZXI Plus', 'Maruti Dzire AMT ZXI Plus'), ('Hyundai Verna CRDi 1.6 SX Option', 'Hyundai Verna CRDi 1.6 SX Option'), ('Hyundai Creta 1.6 SX Diesel', 'Hyundai Creta 1.6 SX Diesel'), ('Maruti Alto LXI', 'Maruti Alto LXI'), ('Jaguar XE 2.0L Diesel Prestige', 'Jaguar XE 2.0L Diesel Prestige'), ('Toyota Etios Liva 1.4 VXD', 'Toyota Etios Liva 1.4 VXD'), ('BMW 5 Series 530i Sport Line', 'BMW 5 Series 530i Sport Line'), ('Maruti Wagon R VXI', 'Maruti Wagon R VXI'), ('Toyota Innova Crysta 2.8 GX AT', 'Toyota Innova Crysta 2.8 GX AT'), ('Skoda Rapid 1.6 MPI Ambition', 'Skoda Rapid 1.6 MPI Ambition'), ('Nissan Micra XV CVT', 'Nissan Micra XV CVT'), ('Mini Cooper 3 DOOR D', 'Mini Cooper 3 DOOR D'), ('Hyundai Grand i10 1.2 CRDi Magna', 'Hyundai Grand i10 1.2 CRDi Magna'), ('Mercedes-Benz GLC 220d 4MATIC Sport', 'Mercedes-Benz GLC 220d 4MATIC Sport'), ('Renault KWID Climber 1.0 AMT', 'Renault KWID Climber 1.0 AMT'), ('Hyundai i20 Active SX Diesel', 'Hyundai i20 Active SX Diesel'), ('Ford Freestyle Titanium Plus Diesel', 'Ford Freestyle Titanium Plus Diesel'), ('Maruti Celerio X VXI Option', 'Maruti Celerio X VXI Option'), ('Hyundai Verna CRDi 1.6 AT SX Plus', 'Hyundai Verna CRDi 1.6 AT SX Plus'), ('Audi Q3 30 TDI Premium FWD', 'Audi Q3 30 TDI Premium FWD'), ('Toyota Etios Cross 1.2L G', 'Toyota Etios Cross 1.2L G'), ('Maruti Vitara Brezza LDi', 'Maruti Vitara Brezza LDi'), ('Volkswagen Vento 1.5 TDI Highline Plus AT', 'Volkswagen Vento 1.5 TDI Highline Plus AT'), ('Toyota Innova Crysta 2.8 GX AT 8S', 'Toyota Innova Crysta 2.8 GX AT 8S'), ('Tata Zest Revotron 1.2T XE', 'Tata Zest Revotron 1.2T XE'), ('Jeep Compass 2.0 Longitude', 'Jeep Compass 2.0 Longitude'), ('Mini Clubman Cooper S', 'Mini Clubman Cooper S'), ('Tata Tiago 1.2 Revotron XZ WO Alloy', 'Tata Tiago 1.2 Revotron XZ WO Alloy'), ('Jeep Compass 1.4 Sport', 'Jeep Compass 1.4 Sport'), ('Jeep Compass 2.0 Sport', 'Jeep Compass 2.0 Sport'), ('Honda WRV i-DTEC VX', 'Honda WRV i-DTEC VX'), ('Skoda Rapid 1.6 MPI AT Style', 'Skoda Rapid 1.6 MPI AT Style'), ('Volkswagen Vento 1.5 TDI Highline', 'Volkswagen Vento 1.5 TDI Highline'), ('Maruti Dzire ZDI', 'Maruti Dzire ZDI'), ('Hyundai Tucson 2.0 e-VGT 4WD AT GLS', 'Hyundai Tucson 2.0 e-VGT 4WD AT GLS'), ('Volkswagen Ameo 1.5 TDI Highline', 'Volkswagen Ameo 1.5 TDI Highline'), ('Mercedes-Benz GLE 250d', 'Mercedes-Benz GLE 250d'), ('Hyundai Xcent 1.2 CRDi SX', 'Hyundai Xcent 1.2 CRDi SX'), ('Skoda Rapid 1.5 TDI AT Ambition', 'Skoda Rapid 1.5 TDI AT Ambition'), ('Honda Brio 1.2 S MT', 'Honda Brio 1.2 S MT'), ('Maruti Baleno Delta CVT', 'Maruti Baleno Delta CVT'), ('Bentley Flying Spur W12', 'Bentley Flying Spur W12'), ('Maruti Alto K10 LXI CNG Optional', 'Maruti Alto K10 LXI CNG Optional'), ('Tata Tiago 1.2 Revotron XT Option', 'Tata Tiago 1.2 Revotron XT Option'), ('Honda Jazz VX CVT', 'Honda Jazz VX CVT'), ('Nissan Micra Active XV', 'Nissan Micra Active XV')], max_length=128)),
                ('Year', models.FloatField(max_length=128)),
                ('Kilometers_Driven', models.FloatField(max_length=128)),
                ('Fuel_Type', models.CharField(choices=[('CNG', 'CNG'), ('Petrol', 'Petrol'), ('Diesel', 'Diesel')], max_length=128)),
                ('Transmission', models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], max_length=128)),
                ('Owner_Type', models.CharField(choices=[('First', 'First'), ('Second', 'Second')], max_length=128)),
                ('Mileage', models.FloatField(max_length=128)),
                ('Engine', models.FloatField(max_length=128)),
                ('Power', models.FloatField(max_length=128)),
                ('Seats', models.FloatField(max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='prediction1',
        ),
    ]