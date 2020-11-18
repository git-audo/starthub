from django.test import TestCase

from board.models import Post

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Post.objects.create(title='Post Title',
                            description='Interesting post description',
                            detailed_description='Even more interesting description',
                            author='Gabriele Creator')

    def test_title_label(self):
        post = Post.objects.get(id=1)
        field_label = author._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'Post Title')        
    


