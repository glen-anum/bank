from django.shortcuts import redirect, render

# Create your views here.
from django.http import JsonResponse
import pandas as pd
from .models import PredResults
from django.contrib.auth.decorators import login_required
import pickle
from .forms import Pred_Results
from sklearn import preprocessing
trans_resultss = preprocessing.LabelEncoder()

def predict(request):
    form = Pred_Results()
    if request.method=="POST":

        # Receive data from client
        
        age = int(request.POST.get('age'))
        gender = request.POST.get('gender')
       
        category= request.POST.get('category')
        amount= float(request.POST.get('amount'))
        # Unpickle model

        gen_pkl = pickle.load(open("predict/ml_models/gender_le.pkl", "rb"))
        
        cate_pkl = pickle.load(open("predict/ml_models/category_test.pkl", "rb"))
        print(age)




        encoded_gen = gen_pkl.transform([gender])
        
        encoded_cat = cate_pkl.transform([category])
        model = pickle.load(open("predict/ml_models/knn.pkl", "rb"))
        result = model.predict([[age, encoded_gen, encoded_cat, amount]])
        classification = result[0]
       




        P=PredResults(age=age,
            gender=gender,
            category=category,
            amount=amount, classification = classification)

        P.save()
        return render(request, 'predict/predict_change.html', {"classification":classification} )
    else:  
        return render(request, 'predict/predict.html', {"form":form})


def predict_chances(request):
    

    

        # Receive data from client
        
       
        # Unpickle model
        
        
        

    return render(request, "predict/predict_change.html")
        

@login_required()
def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults.objects.all()}
    return render(request, "predict/results.html", data)
