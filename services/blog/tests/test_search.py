from django.test import TestCase

from services.blog.apps.post.models import Post


class SearchTest(TestCase):

    def setUp(self):
        self.post1 = Post.objects.create(title='Test Post 1', body='Content for post 1')
        self.post2 = Post.objects.create(title='Another Test Post', body='Content for another post')

    def test_search_posts(self):
        results = Post.objects.search('Test')  # type: ignore
        result_titles = [post.title for post in results]
        self.assertIn(str(self.post1), result_titles)
        self.assertIn(str(self.post2), result_titles)
