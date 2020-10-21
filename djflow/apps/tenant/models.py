from django.db import models
from tenant_schemas.models import TenantMixin


class Client(TenantMixin):
    name = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)
    user = models.OneToOneField("auth.User", on_delete=models.PROTECT, blank=True, null=True)
    auto_create_schema = True

