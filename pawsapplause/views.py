from django.shortcuts import render

def error_400_view(request, exception):
        data = {}
        return render(request,'errorpage/400.html', data)

def error_403_view(request, exception):
        data = {}
        return render(request,'errorpage/403.html', data) 

def error_404_view(request, exception):
        data = {}
        return render(request,'errorpage/404.html', data)

def error_500_view(request):
        data = {}
        return render(request,'errorpage/500.html', data) 
def error_503_view(request,  exception):
        data = {}
        return render(request,'errorpage/503.html', data)
