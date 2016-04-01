Wiki (django-wiki) Template Plugin
==================================

`wiki <https://github.com/django-wiki/django-wiki>`_ is is a rewrite of django-simplewiki,
a project from 2009 that aimed to be a base system for a wiki.

Template Plugin
****************

[**NEED TO TRANSLATE**]

模板插件类似于 MediaWiki 的模板，通过定义模板可在多个文章中使用。

Install
-------

``pip install wiki-template`` and create your django project.


Settings
--------

Insert "wiki_template" to ``INSTALLED_APPS`` before "wiki.plugins.*"::

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'django.contrib.humanize',
        'sekizai',
        'sorl.thumbnail',
        'django_nyt',
        'wiki',
        'wiki.plugins.macros',
        'wiki.plugins.help',
        'wiki.plugins.links',
        'wiki.plugins.images',
        'wiki.plugins.attachments',
        'wiki.plugins.notifications',
        'wiki_template',
        'mptt',
    )

[**NEED TO TRANSLATE**]

设置 ``WIKI_MARKDOWN_KWARGS`` 配置项的 "safe_mode" 键为 ``False``，这样可以在文章和模板中使用html标签::

    WIKI_MARKDOWN_KWARGS = {
        #'extensions': [
        #    ....
        #],
        "safe_mode": False,
    }


Bug report
**********

Any issues report to `Github <https://github.com/tkliuxing/wiki-template/issues>`_.
