from django.shortcuts import render, redirect
from shopping.forms import sampleform
# Create your views here.


def sample(request):
    form = sampleform()
    if request.method == 'POST':
        form = sampleform(request.POST)
        if form.is_valid():
            return redirect('/s/sample/')
    return render(request, 'sample.html', {'form': form})
