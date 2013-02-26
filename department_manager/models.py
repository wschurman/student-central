from django.db import models


class Department(models.Model):
    name = models.TextField()
    short_name = models.CharField(max_length=20)
    office_address = models.ForeignKey('location_manager.Address')

    def __unicode__(self):
        return u'%s' % (self.short_name)
