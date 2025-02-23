from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about_us.html')
def governance(request):
    return render(request, 'governance.html')
def department(request):
    return render(request, 'department.html')
def alumni(request):
    return render(request, 'alumni.html')
def placements(request):
    return render(request, 'placements.html')
def nirf(request):
    return render(request, 'nirf.html')
def off_docs(request):
    return render(request, 'off_docs.html')
def committee(request):
    return render(request, 'committee.html')
def administration(request):
    return render(request, 'administration.html')
def ece(request):
    return render(request, 'ece.html')
def cse(request):
    return render(request, 'cse.html')
def bsc(request):
    return render(request, 'bsc.html')
def docs(request):
    return render(request, 'docs.html')
def progs(request):
    return render(request, 'progs.html')