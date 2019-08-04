from django.test import TestCase
from .forms import ItemForm

# Create your tests here.
class TestToDoItemForm(TestCase):

    '''We test that we can create a  item with only name'''
    def test_can_create_item_with_just_name(self):
        form = ItemForm({'name':'Create test'})
        self.assertTrue(form.is_valid())

    '''Test that the error message is correct if not name is provided'''
    def test_correct_message_for_missing_name(self):
        form = ItemForm({'name':''})
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['name'],[u'This field is required.'])    
