# -*- coding: UTF-8 -*-
####################################################################
#   This file is subject to the terms and conditions defined in
#   file 'LICENSE.txt', which is part of this source code package.
####################################################################

from django.contrib import admin

from {{ app_name }} import models


class FooAdmin(admin.ModelAdmin):
    list_display = ('organization', 'user', 'departement')
    readonly_fields = ('updated', 'created',)


admin.site.register(models.Foo, FooAdmin)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
