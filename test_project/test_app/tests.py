from django.test import TestCase
from .forms import TestFormNewRendering
# written by chatgpt
class MultiWidgetRenderTest(TestCase):
    def test_new_rendering(self):
        form = TestFormNewRendering(initial={'multi_field': 'value1,value2'})
        rendered_html = form.as_p()
        self.assertIn('id_multi_field_0', rendered_html)  # Check for subwidget IDs
        self.assertIn('id_multi_field_1', rendered_html)
