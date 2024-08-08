from django.conf import settings
from django.db import models

from services.catalog.models import Product
from services.models.mixins import CreatedUpdatedMixin


class Order(CreatedUpdatedMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    stripe_id = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['id']),
        ]

    def __str__(self):
        return f'Order {self.id}'  # type: ignore

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())  # type: ignore

    def get_stripe_url(self):
        if not self.stripe_id:  # type: ignore
            # 연결된 결제 없음
            return ''
        if '_test_' in settings.STRIPE_SECRET_KEY:  # type: ignore
            # 테스트 결제를 위한 Stripe 경로
            path = 'test'
        else:
            # 실제 결제를 위한 Stripe 경로
            path = '/'
        return f'https://dashboard.stripe.com/{path}/payments/{self.stripe_id}'  # type: ignore


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.product.name} ({self.quantity})'  # type: ignore

    def get_cost(self):
        return self.price * self.quantity  # type: ignore
