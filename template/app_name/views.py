# -*- coding: UTF-8 -*-
####################################################################
#   This file is subject to the terms and conditions defined in
#   file 'LICENSE.txt', which is part of this source code package.
####################################################################

from django.shortcuts import render_to_response
from django.shortcuts import redirect

from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from {{ app_name }} import models

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
