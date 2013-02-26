from django.db import models


class Person(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )

    name = models.TextField()
    id_number = models.IntegerField()
    id_string = models.CharField(max_length=20)
    email_address = models.EmailField()

    phone_number = models.CharField(max_length=30)
    birth_date = models.DateField()

    address = models.ForeignKey('location_manager.Address')

    gender = models.CharField(max_length=2,
                              choices=GENDER_CHOICES)

    last_modified = models.DateTimeField(auto_now=True, auto_now_add=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        u'%s: %s (%d)' % (self.id_string, self.name, self.id_number)


class Faculty(Person):
    department = models.ForeignKey('department_manager.Department')

    def __unicode__(self):
        return u'%s, %s' % (Person.__unicode__(self), unicode(self.department))


class Student(Person):
    year = models.PositiveIntegerField()
    advisors = models.ManyToManyField(Faculty)

    def __unicode__(self):
        return u'%s, Year: %d' % (Person.__unicode__(self), self.year)
