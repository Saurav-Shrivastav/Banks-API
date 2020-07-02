from django.db import models


class Bank (models.Model):

    id = models.IntegerField(primary_key=True, default=0, editable=False)    
    name = models.CharField(max_length = 50, null = True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'


class Branch (models.Model):

    ifsc = models.CharField(max_length = 11, primary_key = True)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)
    branch = models.CharField(max_length = 100, null = True)
    address = models.CharField(max_length = 300, null = True)
    city = models.CharField(max_length = 200, null = True)
    district = models.CharField(max_length = 200, null = True)
    state = models.CharField(max_length = 100, null = True)

    class Meta:
        ordering = ('branch',)
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'
    
    def __str__(self):
        return f'{self.branch} - {self.city} - {self.bank_id}'