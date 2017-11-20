from django.db import models

# Create your models here.
# class Host(models.Model):
#     hostname = models.CharField(max_length=50, verbose_name=u"主机名", unique=True)
#     ip = models.GenericIPAddressField(u"管理IP", max_length=15)
#     other_ip = models.CharField(u"其它IP", max_length=100, null=True, blank=True)
#     group = models.ForeignKey(HostGroup, verbose_name=u"设备组", on_delete=models.SET_NULL, null=True, blank=True)
#     asset_no = models.CharField(u"资产编号", max_length=50, null=True, blank=True)
#     asset_type = models.CharField(u"设备类型", choices=ASSET_TYPE, max_length=30, null=True, blank=True)
#     status = models.CharField(u"设备状态", choices=ASSET_STATUS, max_length=30, null=True, blank=True)
#     os = models.CharField(u"操作系统", max_length=100, null=True, blank=True)
#     vendor = models.CharField(u"设备厂商", max_length=50, null=True, blank=True)
#     cpu_model = models.CharField(u"CPU型号", max_length=100, null=True, blank=True)
#     cpu_num = models.CharField(u"CPU数量", max_length=100, null=True, blank=True)
#     memory = models.CharField(u"内存大小", max_length=30, null=True, blank=True)
#     disk = models.CharField(u"硬盘信息", max_length=255, null=True, blank=True)
#     sn = models.CharField(u"SN号 码", max_length=60, blank=True)
#     idc = models.ForeignKey(Idc, verbose_name=u"所在机房", on_delete=models.SET_NULL, null=True, blank=True)
#     position = models.CharField(u"所在位置", max_length=100, null=True, blank=True)
#     memo = models.TextField(u"备注信息", max_length=200, null=True, blank=True)
#
#     def __unicode__(self):
#         return self.hostname
#
# class HostGroup(models.Model):
#     name = models.CharField(u"组名", max_length=30, unique=True)
#     desc = models.CharField(u"描述", max_length=100, null=True, blank=True)
#
#     def __unicode__(self):
#         return self.name
#
# class Idc(models.Model):
#     name = models.CharField(u"机房名称", max_length=30, null=True)
#     address = models.CharField(u"机房地址", max_length=100, null=True)
#     tel = models.CharField(u"机房电话", max_length=30, null=True)
#     contact = models.CharField(u"客户经理", max_length=30, null=True)
#     contact_phone = models.CharField(u"移动电话", max_length=30, null=True)
#     jigui = models.CharField(u"机柜信息", max_length=30, null=True)
#     ip_range = models.CharField(u"IP范围", max_length=30, null=True)
#     bandwidth = models.CharField(u"接入带宽", max_length=30, null=True)
#
#     def __unicode__(self):
#         return self.name
#     ###这个属性是定义当前的模型类是不是一个抽象类。所谓抽象类是不会对应数据库表的。一般我们用它来归纳一些公共属性字段，然后继承它的子类可以继承这些字段
#     class Meta:
#         verbose_name = u'数据中心'
#         verbose_name_plural = verbose_name
