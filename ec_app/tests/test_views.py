from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ec_app.models import Customer, CustomerProfile, Order, Product, Category, ProductCategory

class CustomerListCreateAPIViewTestCase(APITestCase):

    def setUp(self):
        self.url = reverse("customer-list")
        self.customer = Customer.objects.create(
            username="test_user",
            email="test@example.com",
            password="test_password",
            first_name="John",
            last_name="Doe"
        )

    def test_list_customers(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_customer(self):
        data = {
            "username": "new_user",
            "email": "new@example.com",
            "password": "new_password",
            "first_name": "Jane",
            "last_name": "Doe"
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 2)

# 同様に他のビューに対応するテストケースを作成してください。
# 例えば、CustomerDetail ビューに対応するテストケースは以下のようになります。

class CustomerRetrieveUpdateDestroyAPIViewTestCase(APITestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            username="test_user",
            email="test@example.com",
            password="test_password",
            first_name="John",
            last_name="Doe"
        )
        self.url = reverse("customer-detail", kwargs={"pk": self.customer.pk})

    def test_retrieve_customer(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], self.customer.username)

    def test_update_customer(self):
        data = {
            "username": "updated_user",
            "email": "updated@example.com",
            "password": "updated_password",
            "first_name": "Updated",
            "last_name": "User"
        }
        response = self.client.put(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.customer.refresh_from_db()
        self.assertEqual(self.customer.username, "updated_user")

    def test_destroy_customer(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Customer.objects.filter(pk=self.customer.pk).exists())

# 他のビュー (
# CustomerProfileList,
# CustomerProfileDetail,
# OrderList,
# OrderDetail,
# ProductList,
# ProductDetail,
# CategoryList,
# CategoryDetail,
# ProductCategoryList,
# ProductCategoryDetail
#
# ) に対しても同様にテストケースを作成してください。
