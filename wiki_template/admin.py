from __future__ import unicode_literals
from __future__ import absolute_import
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from . import models


class TemplateRevisionAdmin(admin.TabularInline):
    model = models.TemplateRevision
    extra = 1
    fields = ('template_content', 'user', 'user_message')


class TemplateAdmin(admin.ModelAdmin):

    inlines = [TemplateRevisionAdmin]

    def article(self, instance):
        return instance.article.current_revision.title
    article.short_description = _('article')

    list_display = ('article', 'template_title', 'extend_to_children',)
    list_display_links = ('article', 'template_title',)

admin.site.register(models.Template, TemplateAdmin)
