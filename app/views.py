from django.shortcuts import render

# Create your views here.
def condition(request):
    d = {'a': 3000,'b':600,'c':900}
    return render(request,'condition.html',d)
