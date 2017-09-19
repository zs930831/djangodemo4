from django.shortcuts import render,redirect,HttpResponse


# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        u = request.POST.get("username")
        p = request.POST.get("pwd")
        # print(p,pwd)
        if u == 'root' and p == '111':
            request.session['u']=u
            request.session['islogin']=True
            return redirect('/index')
        else:
            return render(request, "login.html")

def index(request):
    if(request.session['islogin']):
        return HttpResponse(request.session['u'])
    else:
        return render(request,'login.html')