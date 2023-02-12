"""
自定义的分页组件，以后如果想要使用这个组件，需要做以下几件事：
1.在视图函数中：
def pretty_list(request):
    # 1.根据自己的情况去筛选自己的数据
    queryset = models.Prettynum.objects.all()
    # 2. 实例化分页对象
    page_object = Pagination(request, queryset)

    context = {"search_data": search_data,

               "queryset": page_object.page_queryset,   # 分完页的数据
               "page_string": page_object.html()   # 生成的页码
               }

    return render(request, 'pretty_list.html', context)
2. 在HTML中：

            {% for obj in queryset_user %}
                {{obj.xxx}}
            {% endfor %}

            <div>
                <ul class="pagination">
                    {{ page_string }}
                </ul>
            </div>

"""
from django.http.request import QueryDict
import copy
from django.utils.safestring import mark_safe

class Pagination(object):
    def __init__(self, request, queryset, page_size=10, page_gram="page", plus=5):
        """
        :param request: 请求的对象
        :param queryset:  符合条件的数据
        :param page_size:  每页显示多少条数据
        :param page_gram:  在url中获取分页的参数 如：/pretty/list/?page=1
        :param plus:  显示当前几页或者后几页（页码）
        """
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict
        self.page_gram = page_gram

        page = request.GET.get(page_gram, "1")
        if page.isdecimal():
            page = int(page)
        else:
            page = 1
        self.page = page
        self.page_size = page_size

        self.start = (page - 1) * page_size
        self.end = page * page_size
        self.page_queryset = queryset[self.start:self.end]

        # 数据总条数
        total_count = queryset.count()
        # 总页码
        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.plus = plus

    def html(self):
        # 计算出，显示当前页的前5页、后5页

        if self.total_page_count <= 2 * self.plus + 1:
            start_page = 1
            end_page = self.total_page_count
        else:
            # 数据库中数据多于11页：
            # 当前页 < 5时
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1
            else:
                # 当前页 >5:
                # 当前页+5 >总页面:
                if (self.page + self.plus) > self.total_page_count:
                    start_page = self.total_page_count - 2 * self.plus
                    end_page = self.total_page_count
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus

        # 页码
        page_str_list = []

        self.query_dict.setlist(self.page_gram,[1])

        # 首页
        first_page = '<li><a href="?{}">首页</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(first_page)
        # 上一页
        if self.page > 1:
            self.query_dict.setlist(self.page_gram,[self.page-1])
            prev_page = '<li><a href="?{}">«</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_gram, [1])
            prev_page = '<li><a href="?{}">«</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(prev_page)

        for i in range(start_page, end_page + 1):
            self.query_dict.setlist(self.page_gram,[i])
            if i == self.page:
                ele = '<li class="active"><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            else:
                ele = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)

            page_str_list.append(ele)
        # 下一页
        if self.page < self.total_page_count:
            self.query_dict.setlist(self.page_gram,[self.page + 1])
            last_page = '<li><a href="?{}">»</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_gram, [self.total_page_count])
            last_page = '<li><a href="?{}">»</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(last_page)
        # 尾页
        self.query_dict.setlist(self.page_gram, [self.total_page_count])
        latest_page = '<li><a href="?{}">尾页</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(latest_page)

        search_string = """
                <li>
                    <form style="float:left;margin-left:-1px" method="get">
                        <input name="page"
                               style="position:relative;float:left;display:inline-block;width:52.9px;border-radius:0;height:33.5px"
                               type="text" class="form-control" placeholder="页码">
                        <button style="border-radius:0" class="btn btn-default" type="submit">跳转</button>
                    </form>
                </li>
        """


        page_str_list.append(search_string)




        page_string = mark_safe("".join(page_str_list))
        return page_string
