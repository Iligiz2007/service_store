from django.forms import ModelForm
from .models import Offer
class FormOffer(ModelForm):
    
    class Meta:
        model = Offer
        fields = ('proposed_price','messege')