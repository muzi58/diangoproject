from applogin import models
from django.core.exceptions import ValidationError
from django import forms
from applogin.utils.BootstrapModelform import BootstrapModelform

class UserModelForm(BootstrapModelform):
    name = forms.CharField(min_length=1, label="用户名")

    class Meta:
        model = models.Userinfo
        fields = ["name", "password", "age", "accent", "create_time", "gender", "depart"]

    def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]

        exists = models.Prettynum.objects.filter(mobile=txt_mobile).exists()

        if exists:
            raise ValidationError('手机号已经存在')
        return txt_mobile

class PrettyModelform(BootstrapModelform):
    # mobile = forms.CharField(
    #     label="电话号码",
    #     validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')]  # r'^166[0-9]','号段必须以166开头')
    # )

    class Meta:
        model = models.Prettynum
        # fields = ["mobile", "price","level","status"]
        fields = "__all__"  # 表示所有的字段
        # exclude = ["mobile"]  # 排除某个字段

    def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]

        exists = models.Prettynum.objects.filter(mobile=txt_mobile).exists()

        if exists:
            raise ValidationError('手机号已经存在')
        return txt_mobile

class PrettyEditModelform(BootstrapModelform):
    # mobile = forms.CharField(
    #     label="电话号码",
    #     validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')]  # r'^166[0-9]','号段必须以166开头')
    # )

    class Meta:
        model = models.Prettynum
        # fields = ["mobile", "price","level","status"]
        # fields = "__all__"  # 表示所有的字段
        exclude = ["mobile"]  # 排除某个字段

    # def clean_mobile(self):
    #     txt_mobile = self.cleaned_data["mobile"]
    #
    #     exists = models.Prettynum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
    #
    #     if exists:
    #         raise ValidationError('手机号已经存在')
    #     return txt_mobile