import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from services.shop.apps.orders.models import Order

from .tasks import payment_completed


# 외부시스템으로부터 POST 요청을 받을 때는 CSRF 토큰을 받을 수 없기 때문에
# @csrf_exempt 데코레이터를 상숑하여 해당 뷰에 대한 csrf 검사를 비활성화함
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        # 이벤트의 서명을 확인
        event = stripe.Webhook.construct_event(payload, sig_header, settings.STRIPE_WEBHOOK_SECRET)
    except ValueError:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:  # type: ignore
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event.type == 'checkout.session.completed':
        session = event.data.object
        if session.mode == 'payment' and session.payment_status == 'paid':  # type: ignore
            try:
                # Fulfill the purchase...
                order = Order.objects.get(id=session.client_reference_id)  # type: ignore
            except Order.DoesNotExist:
                return HttpResponse(status=404)
            # 주문을 결제완료로 표시
            order.paid = True
            # Stripe 결제 세션 ID 저장
            order.stripe_id = session.payment_intent  # type: ignore
            order.save()
            # 비동기 작업 실행
            payment_completed.delay(order.id)  # type: ignore
    return HttpResponse(status=200)
