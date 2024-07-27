from decimal import Decimal

import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from services.shop.apps.orders.models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


def payment_process(request):
    order_id = request.session.get('order_id', None)
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        success_url = request.build_absolute_uri(reverse('payment:completed'))
        cancel_url = request.build_absolute_uri(reverse('payment:canceled'))
        # Stripe 결제 세션 데이터
        session_data = {
            'mode': 'payment',
            'client_reference_id': order.id,  # type: ignore
            'success_url': success_url,
            'cancel_url': cancel_url,
            'line_items': []
        }
        # Stripe 결제 세션에 주문 품목 추가
        for item in order.items.all():  # type: ignore
            session_data['line_items'].append(
                {
                    'price_data': {
                        'unit_amount': int(item.price * Decimal('100')),
                        'currency': 'usd',
                        'product_data': {
                            'name': item.product.name,
                        }
                    },
                    'quantity': item.quantity,
                }
            )
        # Stripe 결제 세션 생성
        session = stripe.checkout.Session.create(**session_data)
        # Stripe 결제 양식으로 리디렉션
        return redirect(session.url, code=303)
    else:
        return render(request, 'payment/process.html', locals())


def payment_completed(request):
    return render(request, 'payment/completed.html')


def payment_canceled(request):
    return render(request, 'payment/canceled.html')


# def get_auth_token():
#     url = 'https://api.portone.io/v2/auth/token'
#     headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
#     data = {'apiSecret': settings.PORTONE_API_SECRET}

#     response = requests.post(url, json=data, headers=headers)
#     return response.json().get('data').get('accessToken')

# def request_payment(payment, order_name):
#     token = get_auth_token()
#     url = 'https://api.portone.io/v2/payments/request'
#     headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
#     data = {
#         'storeId': settings.PORTONE_STORE_ID,
#         'paymentId': payment.payment_id,
#         'orderName': order_name,
#         'totalAmount': payment.amount,
#         'currency': 'KRW',
#         'payMethod': 'CARD',
#         'returnUrl': f'{MY_DOMAIN}/payment/success',
#         'cancelUrl': f'{MY_DOMAIN}/payment/cancel',
#     }

#     response = requests.post(url, json=data, headers=headers)
#     return response.json()

# @csrf_exempt
# def payment_callback(request):
#     data = request.POST
#     payment_id = data.get('paymentId')
#     status = data.get('status')

#     try:
#         payment = Payment.objects.get(payment_id=payment_id)
#         payment.status = status
#         payment.save()
#         return JsonResponse({'status': 'success'})
#     except Payment.DoesNotExist:
#         return JsonResponse({'status': 'failed', 'message': 'Payment not found'}, status=404)
