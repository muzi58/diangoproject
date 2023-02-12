from django.middleware.common import CommonMiddleware


class M1(CommonMiddleware):
    """中间件1"""
    # 如果没有返回值（返回None），继续往后走
    # 如果有返回值 HttpResponse 、render 、redirect

    def process_request(self, request):
        print("M1.entering")

    def process_response(self, request, response):
        print("M1.went")
        return response


class M2(CommonMiddleware):
    """中间件2"""

    def process_request(self, request):
        print("M2.entering")

    def process_response(self, request, response):
        print("M2.went")
        return response

