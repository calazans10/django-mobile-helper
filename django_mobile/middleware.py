# -*- coding: utf-8 -*-
import re
from django.conf import settings
from constants import AGENT, VERSION


class MobileMiddleware(object):

    ORIG_TEMPLATE_DIRS = settings.TEMPLATE_DIRS

    def is_mobile_useragent(self, request):
        if 'HTTP_USER_AGENT' in request.META:
            user_agent = request.META['HTTP_USER_AGENT']
            reg_b = re.compile(AGENT, re.I | re.M)
            reg_v = re.compile(VERSION, re.I | re.M)

            b = reg_b.search(user_agent)
            v = reg_v.search(user_agent[0:4])

            if b or v:
                return True

        return False

    def process_request(self, request):
        request.is_mobile = False
        domain = request.META.get('HTTP_HOST', '').split('.')

        if 'm' in domain or 'mobile' in domain:
            request.is_mobile = True
        elif self.is_mobile_useragent(request):
            request.is_mobile = True
        else:
            request.is_mobile = False

        if request.is_mobile:
            settings.TEMPLATE_DIRS = settings.MOBILE_TEMPLATE_DIRS + \
                self.ORIG_TEMPLATE_DIRS
        else:
            settings.TEMPLATE_DIRS = settings.DESKTOP_TEMPLATE_DIRS + \
                self.ORIG_TEMPLATE_DIRS

        return None
