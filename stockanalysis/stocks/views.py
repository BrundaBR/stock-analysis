from django.shortcuts import render,redirect
import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import UserCreationForm
import sqlite3
from .models import BSEdata
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.

def Homepage(request):
    try:
        Stock_code = request.GET['g']
        stock_obtained=BSEdata.objects.filter(security_code=Stock_code)
        return render(request,"index.html",{'stock_obtained':stock_obtained})

        
        
    except MultiValueDictKeyError:
        Stock_code = False
        
    return render(request,"index.html")




def View(request):
    conn = sqlite3.connect("db.sqlite3")
    
    dff=BSEdata.objects.all()
    
    return render(request,'tableview.html',{'dff':dff})
def bhav(request):
    
    if request.user.is_authenticated:
        if request.POST:
            master_date = request.POST['bhav_copy_date']
            excel_file = request.FILES['bhav_copy_file']
            fs = FileSystemStorage(location='static/')
            filename = fs.save(excel_file.name, excel_file)
            
            df = pd.read_csv('static/' + excel_file.name )
            sm_list = df.values.tolist()
            sm_list = sm_list[:]
            for tmp_list in sm_list:
                sm = BSEdata(copy_date=master_date, security_code=tmp_list[0], security_name=tmp_list[1], security_group=tmp_list[2], open=tmp_list[4], high=tmp_list[5], low=tmp_list[6], close=tmp_list[7], last=tmp_list[8], prevclose=tmp_list[9], no_trades=tmp_list[10], no_of_shares=tmp_list[11], net_turnover=tmp_list[12], isin_code=tmp_list[14])
                sm.save()
            os.remove('static/' +excel_file.name)
      
    else:
        
        if request.POST:
            master_date = request.POST['bhav_copy_date']
            excel_file = request.FILES['bhav_copy_file']
            fs = FileSystemStorage(location='static/')
            filename = fs.save(excel_file.name, excel_file)
            
            df = pd.read_csv('static/' + excel_file.name)
            sm_list = df.values.tolist()
            sm_list = sm_list[:]
            for tmp_list in sm_list:
                sm = BSEdata(copy_date=master_date, security_code=tmp_list[0], security_name=tmp_list[1], security_group=tmp_list[2], open=tmp_list[4], high=tmp_list[5], low=tmp_list[6], close=tmp_list[7], last=tmp_list[8], prevclose=tmp_list[9], no_trades=tmp_list[10], no_of_shares=tmp_list[11], net_turnover=tmp_list[12], isin_code=tmp_list[14])
                sm.save()
            os.remove('static/' + excel_file.name)

    return render(request,'upload.html')