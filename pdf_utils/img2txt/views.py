from django.http import request, HttpResponse
from django.shortcuts import render, redirect

import zipfile
import os
import glob

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
            return redirect('img2txt:show_uploaded', task_id)
    else:
        form = ImageForm()

    context = {'form': form}
    return render(request, 'img2txt/upload.html', context)


def show_uploaded(request, task_id):
    path = 'media/img2txt'
    files = glob.glob(path+'/'+task_id+'_*.txt')

    context = {'download_list': files}
    print(context)
    return render(request, 'img2txt/download.html', context)


def download_zip(request):
    # <input type="checkbox" name="zip"のnameに対応
    file_pks = request.POST.getlist('zip')
    upload_files = Image.objects.filter(pk__in=file_pks)

    response = HttpResponse(content_type='application/zip')
    file_zip = zipfile.ZipFile(response, 'w')
    for upload_file in upload_files:
        file_zip.writestr(upload_file.file.name, upload_file.file.read())

    # Content-Dispositionでダウンロードの強制
    response['Content-Disposition'] = 'attachment; filename="txt.zip"'

    return response
