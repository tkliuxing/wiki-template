Wiki (django-wiki) Template Plugin
==================================

`wiki <https://github.com/django-wiki/django-wiki>`_ is is a rewrite of django-simplewiki,
a project from 2009 that aimed to be a base system for a wiki.

Template Plugin
****************

Wiki Template almoust like MediaWiki's template language. One definition, used in multiple places.

Install
-------

``pip install wiki-template`` and create your django project.


Settings
--------

Insert "wiki_template.apps.WikiTemplateConfig" to ``INSTALLED_APPS`` before "wiki.plugins.*"::

    INSTALLED_APPS = [
        ......
        'wiki_template.apps.WikiTemplateConfig',
        ......
    ]


You may need add configure ``WIKI_MARKDOWN_HTML_WHITELIST`` to settings.py
when you want use html into wiki template.

e.g.::

    WIKI_MARKDOWN_HTML_WHITELIST = [
        'center', 'style', 'div'
    ]

Also you need add ``WIKI_MARKDOWN_HTML_ATTRIBUTES``, ``WIKI_MARKDOWN_HTML_STYLES`` to settings when use inline style::

    WIKI_MARKDOWN_HTML_ATTRIBUTES = {
        '*': ['style']
    }

    WIKI_MARKDOWN_HTML_STYLES = [
        'padding', 'width', 'color', 'float', 'clear', 'background'
    ]

Bug report
**********

Any issues report to `Github <https://github.com/tkliuxing/wiki-template/issues>`_.
