from django.middleware.common import CommonMiddleware
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect, render


class AutoMiddleware(MiddlewareMixin):
    """中间件1"""

    def process_request(self, request):

        if request.path_info in ['/login/', '/image/code/']:
            return

        info_dict = request.session.get("info")

        # 判断用户是否登录过
        if info_dict:
            return
        return redirect('/login/')
