from django.db import models

# Create your models here.
# insert into axf_wheel(img,name,trackid)
# values("http://img01.bqstatic.com//upload/activity/2017031716035274.jpg@90Q.jpg","酸奶女王","21870"),
# ("http://img01.bqstatic.com//upload/activity/2017031710450787.jpg@90Q.jpg","优选圣女果","21869"),("http://img01.bqstatic.com//upload/activity/2017030714522982.jpg@90Q.jpg","伊利酸奶大放价","21862"),("http://img01.bqstatic.com//upload/activity/2017032116081698.jpg@90Q.jpg","鲜货直供－窝夫小子","21770"),("http://img01.bqstatic.com//upload/activity/2017032117283348.jpg@90Q.jpg","鲜货直供－狼博森食品","21874");

class Frist(models.Model):
    # 图片
    img = models.CharField(max_length=100)
    # 名称
    name = models.CharField(max_length=100)
    # 商品编号
    trackid = models.CharField(max_length=10)
    class Meta:
        abstract = True

class Wheel(Frist):
    class Meta:
        db_table = 'axf_wheel'


class Nav(Frist):
    class Meta:
        db_table = 'axf_nav'

class Mustbuy(Frist):
    class Meta:
        db_table = 'axf_mustbuy'

class Shop(Frist):
    class Meta:
        db_table = 'axf_shop'

