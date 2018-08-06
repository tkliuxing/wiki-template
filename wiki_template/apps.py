from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WikiTemplateConfig(AppConfig):
    name = 'wiki_template'
    verbose_name = _("Wiki Template")
    label = 'wiki_template'
