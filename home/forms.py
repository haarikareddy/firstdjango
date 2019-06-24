from django import forms
from home.models import Book,Author,Genre

""" class CustomForms(forms.Form):
        username=forms.CharField(
        label='username',
        widget=forms.TextInput(attrs={"placeholder":"your username",'class':'form-control','max':'20'})
    )
    email=forms.EmailField(label='your email',widget=forms.EmailInput(attrs={"placeholder":"lks@gmail.com",'class':'form-control'})) 
"""

class BookForms(forms.Form):
    name=forms.CharField(label='Book Name',widget=forms.TextInput(attrs={"placeholder":"Book name",'maxlength':'30'}))
    #book_author=models.CharField(max_length=100, help_text='Book Author',null=True)
    #purchase_date=models.DateField(null=True,blank=True)
    
    author=forms.ModelChoiceField(queryset=Author.objects.all(),empty_label='Author',widget=forms.Select(attrs={'name':'author','id':'author'}))
    #summary=forms.CharField(label='Summary',widget=forms.Textarea(attrs={'placeholder':'Summary','name':'summary','id':'summary','class':'form-control'}))
    #isbn=forms.CharField(label='ISBN Number',widget=forms.TextInput(attrs={"placeholder":"ISBN Number",'class':'form-control','name':'isbn','id':'isbn'}))
    #genre=forms.ModelMultipleChoiceField(queryset=Genre.objects.all(),widget=forms.CheckboxSelectMultiple)
    pur_date=forms.DateField(label='',widget=forms.DateInput(attrs={'placeholder':'purchase date','name':'pur_date','id':'pur_date','class':'form-control'}))

class modelBookForms(forms.ModelForm):
    name=forms.CharField(label='Book Name',widget=forms.TextInput(attrs={"placeholder":"Book name",'maxlength':'30'}))
    #book_author=models.CharField(max_length=100, help_text='Book Author',null=True)
    #purchase_date=models.DateField(null=True,blank=True)
    
    author=forms.ModelChoiceField(queryset=Author.objects.all(),empty_label='Author',widget=forms.Select(attrs={'name':'author','id':'author'}))
    summary=forms.CharField(label='Summary',widget=forms.Textarea(attrs={'placeholder':'Summary','name':'summary','id':'summary','class':'form-control'}))
    isbn=forms.CharField(label='ISBN Number',widget=forms.TextInput(attrs={"placeholder":"ISBN Number",'class':'form-control','name':'isbn','id':'isbn'}))
    #genre=forms.ModelMultipleChoiceField(queryset=Genre.objects.all(),widget=forms.CheckboxSelectMultiple)
    #pur_date=forms.DateField(label='',widget=forms.DateInput(attrs={'placeholder':'purchase date','name':'pur_date','id':'pur_date','class':'form-control'}))

    class Meta:
        model=Book
        fields='__all__'

class SearchForm(forms.Form):
    q=forms.CharField(label='Book Name',widget=forms.TextInput(attrs={"placeholder":"Search",'class':'form-control','maxlength':'30','minlength':'2'}))
