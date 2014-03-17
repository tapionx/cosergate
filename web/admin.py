from django.contrib import admin
from web.models 	import Environment
from web.models 	import User
from web.models 	import Expenditure
from web.models 	import Product

admin.site.register(Environment)
admin.site.register(User)
admin.site.register(Expenditure)
admin.site.register(Product)
