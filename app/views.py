from django.shortcuts import render,redirect
from . forms import Registration_form ,pin_validation
from . models import account
from .encrypt import hide

# Create your views here.
def index(request):
    return render(request,'home.html')

def register(request):
    msg=''
    form=Registration_form()
    if request.method=="POST":
        form=Registration_form(request.POST)
        if form.is_valid:
            form.save()
            data=account.objects.get(phone=request.POST.get('phone'))
            if data:
                msg=f'your account number is {data.acc_num}'
            print('added')    
    return render(request,'register.html',{'form':form,'msg':msg})

def pin(request):
    msg=''
    form=pin_validation()
    if request.method=="POST":
        form=pin_validation(request.POST)
        if form.is_valid:
            acc=request.POST.get('account_num')
            aadhar=int(request.POST.get('aadhar'))
            pin=request.POST.get('pin')
            c_pin=request.POST.get('c_pin')
            data=account.objects.get(acc_num=acc)
            if data:
                if pin==c_pin:
                    if data.aadhar==aadhar:
                        data.pin=hide(pin)
                        data.save()
                        return redirect('home')
                else:
                    msg='pin mismatched'
    context={
        'form1':form,
        'msg':msg
    }                
    return render(request,'pin.html',context)

def checkBal(request):
    msg=''
    if request.method=="POST":
        acc=request.POST.get('acc')
        pin=request.POST.get('pin')
        data=account.objects.get(acc_num=acc)
        if data:
            if data.pin==hide(pin):
                msg=f'your current balance is {data.bal}'
            else:
                msg='incorrect pin'
    context={
        'msg':msg
    }                
    return render(request,'CheckBalance.html',context)

def deposit(request):
    msg=''
    if request.method=='POST':
        acc=int(request.POST.get('acc'))
        pin=request.POST.get('pin')
        amt=int(request.POST.get('amt'))
        data=account.objects.get(acc_num=acc)
        if data:
            if data.pin==hide(pin):
                if amt>100:
                    data.bal+=amt
                    data.save()
                    return redirect('home')
                else:
                    msg='amount is too low to deposit' 
            else:
                msg='incorrect pin'
    context={
        'msg':msg
    }                        
    return render(request,'transaction.html',context)


def withdraw(request):
    msg=''
    if request.method=='POST':
        acc=int(request.POST.get('acc'))
        pin=request.POST.get('pin')
        amt=int(request.POST.get('amt'))
        data=account.objects.get(acc_num=acc)
        if data:
            if data.pin==hide(pin):
                if amt<=data.bal:
                    data.bal-=amt
                    data.save()
                    msg="amount withdrawn successfully"
                else:
                    msg='insufficient funds' 
            else:
                msg='incorrect pin'
    context={
        'msg':msg,
        'flag':True
    }                        
    return render(request,'transaction.html',context)

def acc_transfer(request):
    msg=''
    if request.method=="POST":
        acc=int(request.POST.get('acc'))
        t_acc=int(request.POST.get('t_acc'))
        pin=request.POST.get('pin')
        amt=int(request.POST.get('amt'))
        data=account.objects.get(acc_num=acc)
        t_data=account.objects.get(acc_num=t_acc)
        if data:
            if data.pin==hide(pin):
                if amt<=data.bal and amt>100:
                    data.bal-=amt

                    if t_data:
                        t_data.bal+=amt
                        t_data.save()
                        data.save()
                        msg='amount transferred successfully'
                else:
                    msg='enter valid amount'
            else:
                msg='incorrect pin'        
    context={
        'msg':msg
    }            
    return render(request,'acc_transfer.html',context)