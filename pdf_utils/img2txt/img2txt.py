import pathlib
import pyocr
from PIL import Image

from .models import Image as Model


def img2txt(task_id):
    img_files = Model.objects.values('image').filter(task_id=task_id)
    txt_dir = pathlib.Path('output_txt/'+task_id)

    tools = pyocr.get_available_tools()
    tool = tools[0]

    index = '1'
    for img_file in img_files:
        print('test')
        print(type(img_file['image']))
        img = Image.open(img_file['image'])
        builder = pyocr.builders.TextBuilder(tesseract_layout=6)
        text = tool.image_to_string(img, lang="jpn+eng", builder=builder)

        path_w = txt_dir/pathlib.Path(index+'.txt')
        with open(path_w, mode='w') as f:
            f.write(text)
            index = int(index)+1
