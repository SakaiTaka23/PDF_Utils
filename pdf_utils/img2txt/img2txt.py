import pathlib
import pyocr
from PIL import Image

from .models import Image as Model


def img2txt(task_id):
    img_files = Model.objects.values('image').filter(task_id=task_id)
    txt_dir = pathlib.Path('media/img2txt/')

    tools = pyocr.get_available_tools()
    tool = tools[0]

    index = '1'
    for img_file in img_files:
        img = Image.open('media/'+img_file['image'])
        builder = pyocr.builders.TextBuilder(tesseract_layout=6)
        text = tool.image_to_string(img, lang="jpn+eng", builder=builder)
        print(text)

        path_w = txt_dir/pathlib.Path(task_id+'_'+index+'.txt')
        with open(path_w, mode='w') as f:
            f.write(text)
            index = str(int(index)+1)
