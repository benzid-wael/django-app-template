# -*- coding: UTF-8 -*-
####################################################################
#   This file is subject to the terms and conditions defined in
#   file 'LICENSE.txt', which is part of this source code package.
####################################################################

from django.conf.urls import patterns, include, url

from {{ app_name }} import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^/foo/?$', views.FooListView.as_view()),
    # url(r'^/foo/(?P<pk>[0-9]+)/?$', views.FooeDetailView.as_view()),


)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
