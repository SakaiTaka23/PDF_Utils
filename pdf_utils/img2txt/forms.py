from django import forms
from .models import Image
from secrets import token_hex


class ImageForm(forms.ModelForm):
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
    )
    task_id = forms.CharField(
        required=False,
        widget=forms.HiddenInput(attrs={'placeholder': ''})
    )

    def clean_task_id(self):
        self.task_id = token_hex(10)
        # while True:
        #     hex = token_hex(10)
        #     if Image.object.get(task_id=hex) == '':
        #         self.task_id = hex
        #         break
        return self.task_id

    class Meta:
        model = Image
        fields = ['image', 'task_id']
