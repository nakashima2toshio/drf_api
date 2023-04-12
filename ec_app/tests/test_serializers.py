from django.test import TestCase
from ec_app.models import Customer, CustomerProfile, Order, Product, Category, ProductCategory
from ec_app.serializers import (
    CustomerSerializer,
    CustomerProfileSerializer,
    OrderSerializer,
    ProductSerializer,
    CategorySerializer,
    ProductCategorySerializer,
)

class CustomerSerializerTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            username="testuser",
            email="test@example.com",
            password="testpassword",
            first_name="Test",
            last_name="User",
        )
        self.serializer = CustomerSerializer(instance=self.customer)

    def test_customer_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {"id", "username", "email", "password", "first_name", "last_name"})
        self.assertEqual(data["username"], self.customer.username)
        self.assertEqual(data["email"], self.customer.email)
        self.assertEqual(data["first_name"], self.customer.first_name)
        self.assertEqual(data["last_name"], self.customer.last_name)

    def test_customer_validation(self):
        invalid_data = {
            "username": "",
            "email": "invalid_email",
            "password": "short",
            "first_name": "",
            "last_name": "",
        }
        serializer = CustomerSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertDictEqual(
            serializer.errors,
            {
                "username": ["This field may not be blank."],
                "email": ["Enter a valid email address."],
                "password": ["Ensure this field has at least 8 characters."],
                "first_name": ["This field may not be blank."],
                "last_name": ["This field may not be blank."],
            },
        )

class CustomerProfileSerializerTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            username="testuser",
            email="test@example.com",
            password="testpassword",
            first_name="Test",
            last_name="User",
        )
        self.profile = CustomerProfile.objects.create(
            customer=self.customer, address="123 Test St", phone_number="1234567890"
        )
        self.serializer = CustomerProfileSerializer(instance=self.profile)

    def test_customer_profile_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {"id", "customer", "address", "phone_number"})
        self.assertEqual(data["customer"], self.profile.customer.id)
        self.assertEqual(data["address"], self.profile.address)
        self.assertEqual(data["phone_number"], self.profile.phone_number)

    def test_customer_profile_validation(self):
        invalid_data = {
            "customer": None,
            "address": "",
            "phone_number": "invalid_phone_number",
        }
        serializer = CustomerProfileSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertDictEqual(
            serializer.errors,
            {
                "customer": ["この項目はnullにできません。"],
                "address": ["この項目は空にできません。"],
                "phone_number": ["Phone number must be entered in the format: '1234567890'."],
            },
        )



class OrderSerializerTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            username="testuser",
            email="test@example.com",
            password="testpassword",
            first_name="Test",
            last_name="User",
        )
        self.order = Order.objects.create(
            customer=self.customer,
            order_date="2022-01-01T00:00:00Z",
            status="processing",
        )
        self.serializer = OrderSerializer(instance=self.order)

    def test_order_fields(self):
        pass  # Add your field tests here

    def test_order_validation(self):
        pass  # Add your validation tests here

class ProductSerializerTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="This is a test product",
            price="9.99",
        )
        self.serializer = ProductSerializer(instance=self.product)

    def test_product_fields(self):
        pass  # Add your field tests here

    def test_product_validation(self):
        pass  # Add your validation tests here

class CategorySerializerTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        self.serializer = CategorySerializer(instance=self.category)

    def test_category_fields(self):
        pass  # Add your field tests here

    def test_category_validation(self):
        pass  # Add your validation tests here

class ProductCategorySerializerTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="This is a test product",
            price="9.99",
        )
        self.category = Category.objects.create(name="Test Category")
        self.product_category = ProductCategory.objects.create(
            product=self.product, category=self.category
        )
        self.serializer = ProductCategorySerializer(instance=self.product_category)

    def test_product_category_fields(self):
        pass  # Add your field tests here

    def test_product_category_validation(self):
        pass  # Add your validation tests here
