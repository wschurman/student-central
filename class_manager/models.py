from django.db import models


class GradeOption(models.Model):
    GRADE_OPTIONS = (
        ('SU', 'Satisfactory/Unsatisfactory'),
        ('SUX', 'Satisfactory/Unsatisfactory Exclusive'),
        ('GRD', 'Graded'),
        ('AUD', 'Audit')
    )

    grade_option = models.CharField(max_length=3, choices=GRADE_OPTIONS)

    def __unicode__(self):
        return u'%s' % self.get_grade_option_display()


class Class(models.Model):
    term = models.ForeignKey('schedule_manager.Term')
    teacher = models.ForeignKey('people_manager.Faculty')

    name = models.TextField()

    department = models.ForeignKey('department_manager.Department')

    location = models.ForeignKey('location_manager.Room')
    number = models.PositiveIntegerField()

    num_credits = models.PositiveIntegerField()

    class_times = models.ManyToManyField('schedule_manager.TimePeriod')

    grade_options = models.ManyToManyField(GradeOption)

    def __unicode__(self):
        return u'%s %s: %s (%s)' % (unicode(self.department), self.number,
                                    self.name, self.term)
