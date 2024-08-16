from django.contrib import admin
from .models import Achievement, Certificates

class CertificatesInline(admin.TabularInline):
    model = Certificates
    extra = 1  # Количество пустых полей для добавления новых сертификатов
    fields = ('image',)  # Поля, которые будут отображаться в инлайн форме

class AchievementAdmin(admin.ModelAdmin):
    list_display = ('name_achievement', 'event_name', 'user', 'status')
    list_filter = ('status',)
    actions = ['verify_achievements', 'reject_achievements']
    inlines = [CertificatesInline]  # Добавляем инлайн-класс

    def verify_achievements(self, request, queryset):
        queryset.update(status='v')
        self.message_user(request, "Selected achievements have been verified.")
    verify_achievements.short_description = "Verify selected achievements"

    def reject_achievements(self, request, queryset):
        queryset.update(status='r')
        self.message_user(request, "Selected achievements have been rejected.")
    reject_achievements.short_description = "Reject selected achievements"

admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Certificates)


# from django.contrib import admin
# from .models import Achievement, Certificates

# class AchievementAdmin(admin.ModelAdmin):
#     list_display = ('name_achievement', 'event_name', 'user', 'status')
#     list_filter = ('status',)
#     actions = ['verify_achievements', 'reject_achievements']

#     def verify_achievements(self, request, queryset):
#         queryset.update(status='v')
#         self.message_user(request, "Selected achievements have been verified.")
#     verify_achievements.short_description = "Verify selected achievements"

#     def reject_achievements(self, request, queryset):
#         queryset.update(status='r')
#         self.message_user(request, "Selected achievements have been rejected.")
#     reject_achievements.short_description = "Reject selected achievements"

# admin.site.register(Achievement, AchievementAdmin)
# admin.site.register(Certificates)
