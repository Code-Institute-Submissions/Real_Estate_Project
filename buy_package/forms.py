from django import forms


class Package(forms.Form):
    quantity = forms.IntegerField(required=True)
    price = 299

    def multiply(self, quantity, price):
        return total == price * quantity

    def return_product(self):
        return self.multiply(self.quantity, self.price)