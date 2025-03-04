from django.contrib import admin
from django.utils.html import format_html
from .models import PersonalInformation, Skill, Project, Service, Certificate, Contact

@admin.register(PersonalInformation)
class PersonalInformationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Information', {
            'fields': ['name', 'title', 'description']
        }),
        ('About Section', {
            'fields': ['about']
        }),
        ('Media', {
            'fields': ['profile_image', 'cv_file']
        }),
        ('Social Links', {
            'fields': ['github', 'linkedin', 'twitter', 'youtube'],
            'classes': ['collapse']
        })
    ]
    list_display = ['name', 'title', 'preview_image']
    
    def preview_image(self, obj):
        if obj.profile_image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; border-radius: 50%;" />', obj.profile_image.url)
        return "-"
    preview_image.short_description = 'Profile Picture'

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'percentage', 'percentage_bar']
    list_editable = ['percentage']
    search_fields = ['name']
    
    def percentage_bar(self, obj):
        return format_html(
            '<div style="width: 100px; background-color: #f0f0f0;">' 
            '<div style="width: {}px; height: 10px; background-color: #2ecc71;"></div>' 
            '</div>', obj.percentage)
    percentage_bar.short_description = 'Progress'

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'preview_image', 'url', 'created_at']
    search_fields = ['title', 'description']
    list_filter = ['created_at']
    
    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: 60px; object-fit: cover;" />', obj.image.url)
        return "-"
    preview_image.short_description = 'Preview'

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon_preview']
    search_fields = ['title', 'description']
    
    def icon_preview(self, obj):
        return format_html('<i class="{}" style="font-size: 20px;"></i>', obj.icon)
    icon_preview.short_description = 'Icon'

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['title', 'preview_image', 'issuing_organization', 'date_received']
    search_fields = ['title', 'issuing_organization']
    list_filter = ['date_received', 'issuing_organization']
    date_hierarchy = 'date_received'
    
    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: 60px; object-fit: cover;" />', obj.image.url)
        return "-"
    preview_image.short_description = 'Preview'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    list_filter = ['created_at']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
    date_hierarchy = 'created_at'
    
    def has_add_permission(self, request):
        return False
