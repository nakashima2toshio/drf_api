from django.test import TestCase
from api.serializers import UserSerializer, CategorySerializer, TaskSerializer
from api.models import CustomUser, Task, Category

class UserSerializerTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')

    def tearDown(self):
        self.user.delete()

    def test_user_serializer(self):
        serializer = UserSerializer(self.user)

        self.assertEqual(serializer.data['username'], 'testuser')

class CategorySerializerTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='TestCategory', slug='test-category')

    def tearDown(self):
        self.category.delete()

    def test_category_serializer(self):
        serializer = CategorySerializer(self.category)

        self.assertEqual(serializer.data['name'], 'TestCategory')
        self.assertEqual(serializer.data['slug'], 'test-category')

class TaskSerializerTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')
        self.category = Category.objects.create(name='TestCategory', slug='test-category')
        self.task = Task.objects.create(user=self.user, title='TestTask', body='TestTaskBody')
        self.task.categories.add(self.category)

    def tearDown(self):
        self.task.delete()
        self.category.delete()
        self.user.delete()

    def test_task_serializer(self):
        serializer = TaskSerializer(self.task)

        self.assertEqual(serializer.data['user']['username'], 'testuser')
        self.assertEqual(serializer.data['title'], 'TestTask')
        self.assertEqual(serializer.data['body'], 'TestTaskBody')
        self.assertEqual(len(serializer.data['categories']), 1)
        self.assertEqual(serializer.data['categories'][0]['name'], 'TestCategory')
いぇs