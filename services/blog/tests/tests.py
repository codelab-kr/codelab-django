# from django.test import TestCase

# from ..models import Post

# class PostModelTest(TestCase):

#     def test_post_model_exists(self):
#         posts = Post.objects.count()
#         self.assertEqual(posts, 0)

#     def test_post_model_has_string_representation(self):
#         post = Post.objects.create(title='Test post')
#         self.assertEqual(str(post), 'Test post')

# class IndexTest(TestCase):

#     def setUp(self):
#         self.post = Post.objects.create(title='Test task')

#     def test_index_page_returns_correct_response(self):
#         response = self.client.get('/')
#         self.assertTemplateUsed(response, 'post/post.html')
#         self.assertEqual(response.status_code, 200)

#     def test_index_page_has_tasks(self):
#         response = self.client.get('/')
#         self.assertContains(response, self.post.title)
