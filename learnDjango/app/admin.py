from django.contrib import admin
from .models import varity, review, cetificate, collage
# Register your models here.

class ChaiReviewInline(admin.TabularInline):
    model = review
    extra = 1

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'createdAt')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('varity',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('cer', 'cer_no', 'issueDate', 'validUntil')

admin.site.register(varity)
admin.site.register(review)
admin.site.register(cetificate, ChaiCertificateAdmin)
admin.site.register(collage, StoreAdmin)


