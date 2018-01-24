from __future__ import absolute_import
from __future__ import unicode_literals
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class TemplateConfig(AppConfig):
    name = 'wiki_template'
    verbose_name = _("Wiki 模板")
    label = 'wiki_template'

default_app_config = 'wiki_template.TemplateConfig'

__version__ = "0.2"
