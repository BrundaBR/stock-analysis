from django.shortcuts import render,redirect
import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import UserCreationForm
import sqlite3
from .models import BSEdata,analysis_01,analysis_02,analysis_03,analysis_04,analysis_05
from django.utils.datastructures import MultiValueDictKeyError
from users.models import SignupForm
# Create your views here.

def Homepage(request):
    try:
        Stock_code = request.GET['g']
        stock_obtained=BSEdata.objects.filter(security_code=Stock_code)
        
        return render(request,"index.html",{'stock_obtained':stock_obtained})

        
        
    except MultiValueDictKeyError:
        Stock_code = False
    user=SignupForm.objects.all()
        
    return render(request,"index.html",{'user':user})




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







#-------------------------------------------------------------

def analysis_1():
    conn=sqlite3.connect("db.sqlite3")
    df=pd.read_sql_query("select * from stocks_bsedata;",conn)
    df["no_trades"]=df["no_trades"].astype(float)
    for i in df.index:
        temp=df.loc[df['security_code']==df['security_code'][i]]
        if ((float(temp['no_trades'].to_string(index=False)))>1000):
            trades=(temp)
            security_name=trades['security_name'].to_string(index=False)
            savee=analysis_01(security_name=security_name)
            savee.save()
def filter_trades_1000(request):
    conn=sqlite3.connect("db.sqlite3")
    df=pd.read_sql_query("select * from stocks_bsedata;",conn)
    #analysis_1()
    dff=pd.read_sql_query("select * from stocks_analysis_01;",conn)
    name=dff['security_name']
    return render(request,"filter_trades_1000.html",{'name':name})

def analysis(request):
    
    return render(request,'analysis.html')
def filter_max_trades(request):
    fil=BSEdata.objects.filter(no_trades=100)
    maximum=fil
    return render(request,'filter_max_trades.html',{'maximum':maximum})