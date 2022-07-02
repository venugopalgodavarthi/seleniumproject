from django.http import HttpResponse
from django.shortcuts import render
from online.forms import collegeform, universityform
from online.models import collegemodel, universitymodel
# creating records
def universityview(request):
    form = universityform
    if request.method == 'POST':
        form = universityform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("data is stored")
    return render(request, 'university.html', {'form': form})


def collegeview(request):
    form = collegeform
    if request.method == 'POST':
        form = collegeform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("data is stored")
    return render(request, 'college.html', {'form': form})

#select the records
def universityviewselect(request):
    res = universitymodel.objects.all()
    return render(request, 'universityselect.html', {'res': res})


def collegeviewselect(request):
    res = collegemodel.objects.all()
    return render(request, 'collegeselect.html', {'res': res})


#update the specific record
def universityviewupdate(request, pk):
    res = universitymodel.objects.get(id=pk)
    form = universityform(instance=res)
    if request.method == 'POST':
        form = universityform(request.POST, instance=res)
        if form.is_valid():
            form.save()
            return HttpResponse("data is stored")
    return render(request, 'university.html', {'form': form})


def collegeviewupdate(request, pk):
    res = collegemodel.objects.get(id=pk)
    form = collegeform(instance=res)
    if request.method == 'POST':
        form = collegeform(request.POST, instance=res)
        if form.is_valid():
            form.save()
            return HttpResponse("data is stored")
    return render(request, 'college.html', {'form': form})

#delete the specific record

def universityviewdelete(request, pk):
    res = universitymodel.objects.get(id=pk)
    if request.method == 'POST':
        universitymodel.objects.get(id=pk).delete()

        return HttpResponse("data is daleted")
    return render(request, 'universitydelete.html', {'res': res})


def collegeviewdelete(request, pk):
    res = collegemodel.objects.get(id=pk)
    if request.method == 'POST':
        collegemodel.objects.get(id=pk).delete()
        return HttpResponse("data is deleted")
    return render(request, 'collegedelete.html', {'res': res})
