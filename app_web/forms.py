from pyexpat import model
from socket import fromshare
from django import forms
from .models import Brand




class BrandForm(forms.ModelForm):

    class Meta:
        model=Brand
        fields=('Name_Brand' , 'Address_Brand' , 'Date_service' , 'software_service')
        labels={
            'Name_Brand':'Brand Name',
            'Address_Brand':'Brand Address',
            'Date_service':'Service Date',
            'software_service':'Software Service'

        }

    def __init__(self, *args, **kwargs):
        super(BrandForm,self).__init__(*args, **kwargs)
        self.fields['software_service'].empty_label= "Select"     
   