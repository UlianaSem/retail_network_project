from django.contrib.admin import ModelAdmin, register, site, action
from django.urls import reverse
from django.utils.html import format_html

from network.models import Company, Contact, Product


site.register(Contact)
site.register(Product)


@register(Company)
class CompanyAdmin(ModelAdmin):
    list_display = ('name', 'company_type', 'link_to_supplier', )
    list_display_links = ('name', 'link_to_supplier', )
    list_filter = ('company_type', 'contacts__city')
    search_fields = ('name', )
    actions = ('clear_indebtedness', )

    @action(description='Clear indebtedness')
    def clear_indebtedness(self, request, queryset):
        queryset.update(indebtedness=None)

    def link_to_supplier(self, obj):
        supplier = obj.supplier

        if supplier:
            url = reverse('admin:network_company_change', args=[supplier.id])
            return format_html('<a href="{}">{}</a>', url, supplier)

        return 'No supplier'
