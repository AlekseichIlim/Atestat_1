from django.contrib import admin
from django.db.models import QuerySet

from sales_network.models import NetworkLink, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model',)
    search_fields = ('title', 'model',)

@admin.register(NetworkLink)
class NetworkLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'city', 'provider', 'arrears', 'email', 'email_provider')
    list_filter = ('city',)
    search_fields = ('level', 'provider', 'city')
    actions = ['clean_arrears']
    # readonly_fields = ('get_email_provider',)

    @admin.display(description='Ссылка на поставщика')
    def email_provider(self, obj: NetworkLink):
        pr = obj.provider
        return pr

    @admin.action(description='Очистить задолжность')
    def clean_arrears(self, request, qs: QuerySet):
        qs.update(arrears=0)
