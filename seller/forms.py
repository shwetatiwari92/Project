from django.forms import ModelForm
from .models import *

class SellerForm(ModelForm):
    class Meta:
        model = Seller
        fields = ('full_name', 'pic', 'gst_no')
