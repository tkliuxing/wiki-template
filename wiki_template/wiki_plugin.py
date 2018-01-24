# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from django.utils.translation import ugettext as _
from django.conf.urls import url
from wiki.core.plugins import registry
from wiki.core.plugins.base import BasePlugin
from . import settings, models, views

from .markdown_extensions import TemplateExtension

from wiki.plugins.notifications.settings import ARTICLE_EDIT
from wiki.plugins.notifications.util import truncate_title


class TemplatePlugin(BasePlugin):

    slug = settings.SLUG
    sidebar = {'headline': _('Template'),
               'icon_class': 'fa fa-files-o',
               'template': 'wiki_template/sidebar.html',
               'form_class': None,
               'get_form_kwargs': (lambda a: {})}
    urlpatterns = {
        'article': [
            url(r'^$',
                views.TemplateView.as_view(),
                name='template_index'
            ),
            url(r'^create/$',
                views.TemplateCreateView.as_view(),
                name='template_create'
            ),
            url(r'^search/$',
                views.TemplateSearchView.as_view(),
                name='template_search'
            ),
            url(r'^(?P<template_id>\d+)/add/to/article/$',
                views.TemplateAddView.as_view(),
                name='template_add_to_article'
            ),
            url(r'^history/(?P<template_id>\d+)/$',
                views.TemplateHistoryView.as_view(),
                name='template_history'
            ),
            url(r'^delete/(?P<template_id>\d+)/$',
               views.TemplateDeleteView.as_view(),
               name='template_delete'
            ),
            url(r'^change/(?P<template_id>\d+)/revision/(?P<revision_id>\d+)/$',
               views.TemplateChangeRevisionView.as_view(),
               name='template_revision_change'
            ),
            url(r'^json/query-title/$',
                views.QueryTitle.as_view(),
                name='template_query_title'
            ),
            url('^(?P<template_id>\d+)/revision/add/$',
                views.RevisionAddView.as_view(),
                name='template_add_revision'
            ),
            url('^(?P<template_id>\d+)/revision/add/preview/$',
                views.EditPreview.as_view(),
                name='template_add_revision_preview'
            ),
            url('^create/preview/$',
                views.CreatePreview.as_view(),
                name='template_create_preview'
            ),
        ]
    }

    article_tab = (_('Template'), "fa fa-files-o")
    article_view = views.TemplateView().dispatch

    # List of notifications to construct signal handlers for. This
    # is handled inside the notifications plugin.
    notifications = [{
        'model': models.TemplateRevision,
        'message': lambda obj: _("A tempalte was changed: %s") % truncate_title(obj.template.template_title),
        'key': ARTICLE_EDIT,
        'created': True,
        'get_article': lambda obj: obj.template.article}
    ]

    markdown_extensions = [TemplateExtension(), ]

    def __init__(self):
        pass

registry.register(TemplatePlugin)
