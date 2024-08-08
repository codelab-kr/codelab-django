import csv
import datetime

from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Order, OrderItem


def order_detail(obj):
    url = reverse('orders:admin_order_detail', args=[obj.id])
    return mark_safe(f'<a href="{url}">View</a>')


def order_payment(obj):
    url = obj.get_stripe_url()
    if obj.stripe_id:
        return mark_safe(f'<a href="{url}" target="_blank">{obj.stripe_id}</a>')
    return ''


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={opts.verbose_name}.csv'
    # CSV 파일의 인코딩을 UTF-8로 설정
    response.write('\ufeff'.encode('utf8'))  # BOM (Byte Order Mark) 추가
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]

    # 헤더 정보로 첫 행 작성
    writer.writerow([field.verbose_name for field in fields])
    # 각 행의 데이터 작성
    for order in queryset:
        data_row = []
        for field in fields:
            value = getattr(order, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response


def order_pdf(obj):
    url = reverse('orders:admin_order_pdf', args=[obj.id])
    return mark_safe(f'<a href="{url}">PDF</a>')


order_payment.short_description = 'Stripe payment'  # type: ignore[attr-defined]
export_to_csv.short_description = 'Export to CSV'  # type: ignore[attr-defined]
order_pdf.short_description = 'Invoice'  # type: ignore[attr-defined]


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    list_display.remove('stripe_id')
    list_display += [order_payment, order_detail, order_pdf]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    actions = [export_to_csv]
