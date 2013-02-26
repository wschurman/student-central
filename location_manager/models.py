from django.db import models


class Address(models.Model):
    TYPES_CHOICES = (
        ('HOME', 'Home'),
        ('WORK', 'Work'),
        ('OTHER', 'Other')
    )

    addr_type = models.CharField(max_length=20, choices=TYPES_CHOICES)

    street_line1 = models.TextField()
    street_line2 = models.TextField()
    city = models.TextField()
    state = models.TextField()
    province = models.TextField()
    code = models.TextField()
    country = models.TextField()

    def __unicode__(self):
        return u'%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s' % (self.get_addr_type_display(),
                                                    self.street_line1,
                                                    self.street_line2,
                                                    self.city,
                                                    self.state,
                                                    self.province,
                                                    self.code,
                                                    self.country)


class Location(models.Model):
    name = models.TextField()
    address = models.ForeignKey(Address)
    # TODO: lat, lng

    def __unicode__(self):
        return u'%s\n%s' % (self.name, unicode(self.address))


class Room(models.Model):
    number = models.CharField(max_length=20)
    building = models.ForeignKey(Location)

    def __unicode__(self):
        return u'%s\n%s' % (self.number, unicode(self.building))
