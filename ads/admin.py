from django.contrib import admin
from .models import Category
from .models import Plan
from .models import Company
from .models import PhoneCompany
from .models import Item
from .models import Link
from .models import LinksCompany
from .models import Image
from .models import Map
from .models import DetPlan





# Register your models here.


admin.site.register(Category)
admin.site.register(Plan)
admin.site.register(Company)
admin.site.register(PhoneCompany)
admin.site.register(Item)
admin.site.register(Link)
admin.site.register(LinksCompany)
admin.site.register(Image)
admin.site.register(Map)
admin.site.register(DetPlan)
