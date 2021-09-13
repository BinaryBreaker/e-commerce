from django import forms




class Product(forms.Form):
    title = forms.CharField(max_length=500)
    Price = forms.IntegerField()
    description = forms.Textarea()
    TITLE_CHOICES = [
        ('MR', 'Mr.'),
        ('MRS', 'Mrs.'),
        ('MS', 'Ms.'),
    ]
    favorite_fruit = forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=TITLE_CHOICES))
    Brand = forms.CharField(max_length=300)
    tags = forms.CharField(max_length=500)
    Stock = forms.IntegerField()
