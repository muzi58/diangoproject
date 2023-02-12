from django.db import models


# Create your models here.
class Department(models.Model):
    """部门表"""

    def __str__(self):
        return self.tittle

    # id = models.BigAutoField(verbose_name='ID',primary_keys=True)#自增id
    tittle = models.CharField(verbose_name="标题", max_length=32)


class Userinfo(models.Model):
    """员工表"""
    name = models.CharField(verbose_name="姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=24)
    age = models.IntegerField(verbose_name="年龄")  # 整形可以不用加长度
    accent = models.DecimalField(verbose_name="余额", max_digits=10, decimal_places=2, default=0)  # 小数2位，默认值为0
    create_time = models.DateField(verbose_name="入职时间")

    # 外键约束
    # to ->关联的哪张表 to_field ->关联的哪一列
    # django会自动生成数据列 -> depart_id
    depart = models.ForeignKey(verbose_name="部门", to="Department", to_field="id", on_delete=models.SET_NULL, null=True,
                               blank=True)
    # 如果部门删除了，解决办法；
    # 1. 级联删除on_delete=models.CASCADE（将部门下属员工资料全部删除）
    # 2. 置空 在原表上加上 on_delete=models.SET_NULL(),null=True,blank=True

    gender_choice = {
        (1, "男"),
        (2, "女")
    }
    # choice django内部约束
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choice)
    from django.db import models

    # Create your models here.


class Prettynum(models.Model):
    mobile = models.CharField(max_length=11, verbose_name="手机号")

    price = models.IntegerField(verbose_name="价格")
    level_choice = (
        (1, "A"),
        (2, "B"),
        (3, "C"),
        (4, "D")
    )

    level = models.SmallIntegerField(choices=level_choice, verbose_name="等级")

    status_choice = (
        (1, "以占用"),
        (2, "未占用")
    )
    status = models.SmallIntegerField(choices=status_choice, verbose_name="状态", default=2)

class Admin(models.Model):
    name = models.CharField(verbose_name="用户名",max_length=16)
    pwd = models.CharField(verbose_name="密码",max_length=32)
