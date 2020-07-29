from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class Goodtext(models.Model):
    """
    测试模型类中chices选项的使用
    """
    STATUS_CHOLCES=(
        (0,"下架"),
        (1,"上架")
    )
    status=models.SmallIntegerField(choices=STATUS_CHOLCES,verbose_name="商品的状态")
    detail = HTMLField(verbose_name="商品的详情")
    content = models.TextField()

    class Meta:
        db_table="df_goods_text"
        verbose_name="商品SKU"
        verbose_name_plural=verbose_name