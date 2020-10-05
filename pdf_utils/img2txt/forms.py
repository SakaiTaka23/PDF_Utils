from django import forms
from .models import Image
from secrets import token_hex


class ImageForm(forms.ModelForm):
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
    )
    task_id = forms.CharField(
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Image
        fields = ['image', 'task_id']


def make_task_id():
    while True:
        hex = token_hex(10)
        if Image.object.get(task_id=hex) == '':
            task_id = hex
            break

    return task_id
