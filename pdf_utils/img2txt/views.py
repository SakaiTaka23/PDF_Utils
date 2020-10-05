from django.shortcuts import render, redirect

from .models import Image
from .forms import ImageForm
# Create your views here.


def showall(request):
    images = Image.objects.all()
    context = {'images': images}
    return render(request, 'img2txt/showall.html', context)


def upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('img2txt:showall')
    else:
        form = ImageForm()

    context = {'form': form}
    return render(request, 'img2txt/upload.html', context)
