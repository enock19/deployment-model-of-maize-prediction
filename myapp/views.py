from django.shortcuts import render,redirect
import joblib
import pandas as pd
from .models import Data
from django.http import HttpResponse
from sklearn.ensemble import RandomForestClassifier

# Create your views here.
def index(request):

      if request.method == 'POST':
            nitrogen = float(request.POST['nitrogen'])
            phosphorus = float(request.POST['phosphorus'])
            potassium = float(request.POST['potassium'])
            temperature = float(request.POST['temperature'])
            humidity = float(request.POST['humidity'])
            ph = float(request.POST['ph'])
            rainfall = float(request.POST['rainfall'])

            #deploy the model
            model = joblib.load('saved_model/ml_model.joblib')

            lis = []

            lis.append(nitrogen)
            lis.append(phosphorus)
            lis.append(potassium)
            lis.append(temperature)
            lis.append(humidity)
            lis.append(ph)
            lis.append(rainfall)

            print(lis)
            #MODEL PREDICTION
            prediction = model.predict([lis])[0]

            #sending the prediction into the database
            Data.objects.create(
                nitrogen=nitrogen,
                phosphorus = phosphorus,
                potassium = potassium,
                temperature = temperature,
                humidity = humidity,
                ph = ph,
                rainfall = rainfall,
                prediction = prediction)
            return render(request, 'result.html', {'prediction_result':prediction})
      return render(request,'predict.html')
      
#fetching the data from the database
def record(request):
      prediction = Data.objects.all() # fetching all the data from the database

      context = {'prediction':prediction}
      return render(request,'database.html',context)

def generate_excel(request):
     
    # Create a HttpResponse object with Excel headers
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="Maize_Prediction.xlsx"'

    # Example data fetching
    data = Data.objects.all().values('nitrogen', 'phosphorus', 'potassium','temperature','humidity','ph','rainfall','prediction')
    df = pd.DataFrame(list(data))

    # Write data to Excel file
    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')

    return response
      

       

       
   
