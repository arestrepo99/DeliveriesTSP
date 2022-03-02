from django import forms
from .models import Product, Client, Order, OrderProduct

class Add_Product(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Product
        fields = "__all__"

class Add_Client(forms.ModelForm):
    #Client
    class Meta:
        model = Client
        fields = "__all__"

class Add_Order(forms.Form):    
    #Order
    client_name = forms.CharField(max_length=30, required=True)
    address = forms.CharField(max_length=30, required=True)
    #product = forms.CharField(max_length=30, required=True)
    #quantity = forms.IntegerField(required=True)
    
    def save(self):
        name = self.cleaned_data.get("client_name")
        address = self.cleaned_data.get("address")
        
        try:
            client = Client.objects.get(
                name = name,
                address = address)
        except Client.DoesNotExist:
            client = Client(
                name = name,
                address = address)
            client.save()
        order = Order(client=client)
        order.save()
        return order

class Add_Product_To_Order(forms.ModelForm):
    #OrderProduct
    def addOrder(self,order):
        self.order = order

    class Meta:
        model = OrderProduct
        fields = ['product', 'quantity']


OrderProductFormSet = forms.formset_factory(Add_Product_To_Order, extra=2)

# class Add_Order(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = '__all__'

# class Add_Client(forms.ModelForm):
#     class Meta:
#         model = Client
#         fields = '__all__'

# class Add_Order_Product(forms.ModelForm):
#     class Meta:
#         model = OrderProduct
#         fields = '__all__'