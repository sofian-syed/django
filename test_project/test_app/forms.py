from django import forms
from django.forms.widgets import TextInput, MultiWidget

# Custom MultiWidget with a decompress method
class CustomMultiWidget(MultiWidget):
    def decompress(self, value):
        """
        Split the single value into a list of values for each subwidget.
        """
        if value:
            return value.split(",")  # Assuming the input is a comma-separated string
        return ["", ""]  # Provide default values if value is None

class TestFormNewRendering(forms.Form):
    multi_field = forms.MultiValueField(
        fields=[forms.CharField(), forms.CharField()],
        widget=CustomMultiWidget(widgets=[TextInput(), TextInput()])  # Use CustomMultiWidget
    )
