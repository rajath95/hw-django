
from django.db import models
from djmoney.models.fields import MoneyField



class Books(models.Model):
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    price=MoneyField(
        decimal_places=2,
        default=0,
        default_currency='USD',
        max_digits=11,
    )

    def __str__(self):
        return self.title

RATINGS= (
('1','1'),
('2','2'),
('3','3'),
('4','4'),
('5','5')
)

BOOKS= (
('FIGHT CLUB', 'Fight Club'),
('CHOKE','Choke'),
('ADJUSTMENT DAY','Adjustment Day')
)




class Feedback(models.Model):

    name=models.CharField(max_length=20)
    title=models.CharField(max_length=22,choices=BOOKS)
    rating = models.CharField(max_length=5,choices=RATINGS,default='4')
    desc=models.CharField(max_length=200)

    def __str__(self):
        return self.name
