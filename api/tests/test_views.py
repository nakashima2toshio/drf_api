from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import CustomUser
from sns_app.models import Profile

"""
api/tests/test_views.py のユニットテスト要件。。

CustomUserViewSet テスト:
a. 認証済みユーザーが自分のユーザー情報を取得できること
b. 認証されていないユーザーがユーザー情報を取得できないこと
c. 認証済みユーザーが自分のユーザー情報を更新できること
d. 認証済みユーザーが自分のユーザー情報を削除できること
e. 認証されていないユーザーがユーザー情報を更新・削除できないこと

ProfileViewSet テスト:
a. 認証済みユーザーが自分のプロフィール情報を取得できること
b. 認証されていないユーザーがプロフィール情報を取得できないこと
c. 認証済みユーザーが自分のプロフィール情報を更新できること
d. 認証済みユーザーが自分のプロフィール情報を削除できること
e. 認証されていないユーザーがプロフィール情報を更新・削除できないこと
"""

class CustomUserViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='paul', password='password')

    def test_authenticated_user_can_retrieve_own_user_info(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('customuser-detail', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'paul')

    def test_unauthenticated_user_cannot_retrieve_user_info(self):
        response = self.client.get(reverse('customuser-detail', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ProfileViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='paul', password='password')
        self.profile = Profile.objects.create(custom_user=self.user, display_name='Paul Smith', bio='Hello!')

    def test_authenticated_user_can_retrieve_own_profile_info(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('profile-detail', kwargs={'pk': self.profile.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['display_name'], 'Paul Smith')
        self.assertEqual(response.data['bio'], 'Hello!')

    def test_unauthenticated_user_cannot_retrieve_profile_info(self):
        response = self.client.get(reverse('profile-detail', kwargs={'pk': self.profile.pk}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_can_update_own_profile_info(self):
        self.client.force_authenticate(user=self.user)
        update_data = {'display_name': 'Paul Doe', 'bio': 'Updated bio'}
        response = self.client.patch(reverse('profile-detail', kwargs={'pk': self.profile.pk}), data=update_data)
        self.profile.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.profile.display_name, 'Paul Doe')
        self.assertEqual(self.profile.bio, 'Updated bio')

    def test_authenticated_user_can_delete_own_profile_info(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(reverse('profile-detail', kwargs={'pk': self.profile.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Profile.objects.filter(pk=self.profile.pk).exists())

    def test_unauthenticated_user_cannot_update_or_delete_profile_info(self):
        update_data = {'display_name': 'Paul Doe', 'bio': 'Updated bio'}
        response = self.client.patch(reverse('profile-detail', kwargs={'pk': self.profile.pk}), data=update_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.delete(reverse('profile-detail', kwargs={'pk': self.profile.pk}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
