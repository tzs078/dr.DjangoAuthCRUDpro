from django.shortcuts import render, redirect
from DocApp.models import *
from django.contrib import messages
from django.contrib.auth import login, logout , authenticate
# Create your views here.

# home secsion------------

def homePage(req):
    doc_view = DocModel.objects.all()
    context = {
        'doc_view' : doc_view
    }
    return render(req,'home.html',context)

def homeDetailsPage(req,id):
    doc_view = DocModel.objects.get(id = id)
    context = {
        'doc_view' : doc_view
    }
    return render(req,"homeDetails.html",context)


# singin login secsion -------
def signupPage(req):
    if req.method == 'POST':
        nameV = req.POST.get('firstname')
        emailV = req.POST.get('emailf')
        password = req.POST.get('passwordf')
        password2 = req.POST.get('passwordf2')

        user_exit = UserModel.objects.filter(username = nameV).exists()

        if user_exit:
            messages.warning(req,'User already Exit')
            return redirect('signupPage')

        if password == password2:
            UserModel.objects.create_user(
                username = nameV,
                email = emailV,
                password = password,
            )
            return redirect('loginPage')
        
        else:
            messages.warning(req,'Invalid password')
            return redirect('signupPage')

    return render (req,'signup.html')

def loginPage(req):
    if req.method == 'POST':
        nameV = req.POST.get('firstname')
        password = req.POST.get('passwordf')

        user = authenticate(username = nameV , password = password )

        if user:
            messages.success(req,'Login Successfully!!!')
            login(req,user)
            return redirect('homePage')


        else:
            messages.warning(req,'Invalid password and username')
            return redirect('loginPage')


    return render(req,'login.html')


def logoutPage(req):
    logout(req)
    return redirect('loginPage')

# CRUD Seccsion----------

def docListPage(req):
    filter_option = req.GET.get('gender')

    doc_data = DocModel.objects.all()

    if filter_option:
        doc_data = DocModel.objects.filter(Gender = filter_option)
    else:
        doc_data = DocModel.objects.all()
         
    context = {
        'doc_data' : doc_data
    }
    return render(req,'docList.html',context)

def docAddPage(req):
    if req.method == 'POST':
        nameV = req.POST.get('firstname')
        emailV = req.POST.get('emailf')
        phoneV = req.POST.get('phonef')
        addressV = req.POST.get('addressf')
        genderV = req.POST.get('Gender')
        imageV = req.FILES.get('imagef')

        DocModel.objects.create(
            Name = nameV,
            Email = emailV,
            Phone = phoneV,
            Address = addressV,
            Gender = genderV,
            Image = imageV,
        )

        return redirect('docListPage')

    return render(req,'docAddPage.html')

def docDltPage(req,id):
    doc = DocModel.objects.get(id = id)
    doc.delete()

    return redirect('docListPage')

def docUpdatePage(req,id):
    doc_data = DocModel.objects.get(id = id)
    if req.method == 'POST':
        nameV = req.POST.get('firstname')
        emailV = req.POST.get('emailf')
        phoneV = req.POST.get('phonef')
        addressV = req.POST.get('addressf')
        genderV = req.POST.get('Gender')
        imageV = req.FILES.get('imagef')

        doc_data.Name = nameV
        doc_data.Email = emailV
        doc_data.Phone = phoneV
        doc_data.Address = addressV
        doc_data.Gender = genderV
        if imageV:
            doc_data.Image = imageV
        doc_data.save()

        return redirect('docListPage')
    
    context = {
        'doc_data' : doc_data
    }
    return render(req,'docUpdate.html',context)


