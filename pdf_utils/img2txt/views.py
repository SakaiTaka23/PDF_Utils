from django.shortcuts import render, redirect

from .models import Image
from .forms import ImageForm
from . import img2txt
# Create your views here.


def showall(request):
    images = Image.objects.all()
    context = {'images': images}
    return render(request, 'img2txt/showall.html', context)


def upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            images = request.FILES.getlist('image', False)
            task_id = form.cleaned_data.get('task_id')
            index = '1'
            print('task_id:', task_id)
            for image in images:
                image.name = task_id+'_'+index+'.jpg'
                image_instance = Image(
                    image=image,
                    task_id=task_id,
                )
                image_instance.save()
                index = str(int(index)+1)
            img2txt.img2txt(task_id)
            # form.save()
            return redirect('img2txt:showall')
    else:
        form = ImageForm()

    context = {'form': form}
    return render(request, 'img2txt/upload.html', context)
