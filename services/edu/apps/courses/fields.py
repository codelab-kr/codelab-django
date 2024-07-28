from django.db import models


class OrderField(models.PositiveIntegerField):

    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields = for_fields
        super(OrderField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        if getattr(model_instance, self.attname) is None:
            # no current value
            try:
                qs = self.model.objects.all()
                if self.for_fields:
                    query = {field: getattr(model_instance, field) for field in self.for_fields}
                    qs = qs.filter(**query)
                last_item = qs.order_by('-order').first()
                if last_item:
                    value = last_item.order + 1  # type: ignore
                else:
                    value = 0
            except self.model.DoesNotExist:
                value = 0
            setattr(model_instance, self.attname, value)
            return value
        else:
            return getattr(model_instance, self.attname)
