from django.http import HttpResponse
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
    file_pks = request.POST.getlist('zip')
    # print('file_pks', file_pks)
    # file_pks['media/img2txt/184ddecfb7c5f9c48e7f_2.txt',
    #          'media/img2txt/184ddecfb7c5f9c48e7f_1.txt']
    response = HttpResponse(content_type='application/zip')

    with zipfile.ZipFile(response, 'w', compression=zipfile.ZIP_DEFLATED) as new_zip:
        count = '1'
        for file_pk in file_pks:
            new_zip.write(file_pk, arcname=count+'.txt')
            count = str(int(count)+1)

    # Content-Dispositionでダウンロードの強制
    response['Content-Disposition'] = 'attachment; filename="result_txt.zip"'

    return response
