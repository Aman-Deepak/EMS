from django.contrib import admin

# Register your models here.
from .models import employee_detail
admin.site.register(employee_detail)

from .models import salary_detail
admin.site.register(salary_detail)