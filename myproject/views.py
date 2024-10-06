from django.shortcuts import render,redirect
from myapp.models import *

def base(req):
    return render(req,'base.html')

def home(req):
    return render(req,'home.html')

def bookview(req):
    data=bookmodel.objects.all()
    text={
        'books':data
    }
    return render(req,'bookview.html',text)

def bookcreate(req):
    if req.method=='POST':
        sname=req.POST.get('name')
        swritter=req.POST.get('writter')
        simg=req.FILES.get('img')
        spublished_date=req.POST.get('published_date')
        stype=req.POST.get('type')

        books=bookmodel(
            name=sname,
            writter=swritter,
            img=simg,
            published_date=spublished_date,
            type=stype,
        )
        books.save()
        return redirect('bookview')
    return render(req,'bookcreate.html')

def deletepage(req, id):
    data=bookmodel.objects.filter(id=id)
    data.delete()    
    return redirect("bookview")

def book(req,id):
    data=bookmodel.objects.filter(id=id)
    return render(req,'index.html',{'data':data})

def editpage(req, id):
    data=bookmodel.objects.filter(id=id)   
    return render(req,"editpage.html",{'data':data})

def update(req):
    if req.method=='POST':
        bid=req.POST.get('id')
        bname=req.POST.get('name')
        bwritter=req.POST.get('writter')
        bimg=req.FILES.get('img')
        bpublished_date=req.POST.get('published_date')
        btype=req.POST.get('type')
        old_img=req.POST.get('old_img')

        up=bookmodel(
            id=bid,
            name=bname,
            writter=bwritter,
            published_date=bpublished_date,
            type=btype,
        )
        if bimg:
            up.img=bimg
            up.save()
        else:
            up.img=old_img
            up.save()

    return redirect("bookview")