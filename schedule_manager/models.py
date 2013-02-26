from django.db import models


class TimePeriod(models.Model):
    DAYS_OF_WEEK = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )

    start_time = models.TimeField()
    end_time = models.TimeField()

    day_of_week = models.IntegerField(max_length=1, choices=DAYS_OF_WEEK)

    def __unicode__(self):
        return u'%s (%s - %s)' % (self.get_day_of_week_display(),
                                  self.start_time, self.end_time)


class Term(models.Model):
    FALL = 'FA'
    SPRING = 'SP'
    SUMMER = 'SU'
    WINTER = 'WI'
    TERM_CHOICES = (
        (FALL, 'Fall'),
        (SPRING, 'Spring'),
        (SUMMER, 'Summer'),
        (WINTER, 'Winter')
    )
    term = models.CharField(max_length=2,
                            choices=TERM_CHOICES)

    year = models.PositiveIntegerField()

    def __unicode__(self):
        return u'%s%d' % (self.get_term_display(), self.year)


class EnrollmentPeriod(models.Model):
    PRE_ENROLL = 'P'
    NORMAL_ENROLL = 'N'
    ENROLL_TYPE_CHOICES = (
        (PRE_ENROLL, 'Pre-Enroll'),
        (NORMAL_ENROLL, 'Normal Enrollment')
    )

    class_year = models.PositiveIntegerField()
    term = models.ForeignKey(Term)

    enroll_type = models.CharField(max_length=1,
                                   choices=ENROLL_TYPE_CHOICES)

    enrollment_start = models.DateTimeField()
    enrollment_end = models.DateTimeField()

    def __unicode__(self):
        return u'%s, %d, %s, %s - %s' % (unicode(self.term), self.class_year,
                                         self.get_enroll_type_display(),
                                         self.enrollment_start,
                                         self.enrollment_end)


class ClassGradeOption(models.Model):
    grade_option = models.ForeignKey('class_manager.GradeOption')
    cclass = models.ForeignKey('class_manager.Class')

    def __unicode__(self):
        return u'%s, %s' % (unicode(self.grade_option), unicode(self.cclass))


class Schedule(models.Model):

    student = models.ForeignKey('people_manager.Student',
                                on_delete=models.PROTECT)

    term = models.ForeignKey(Term)

    classes = models.ManyToManyField('class_manager.Class',
                                     symmetrical=False)

    grade_options = models.ManyToManyField(ClassGradeOption)

    def __unicode__(self):
        class_list = '\n'.join(self.classes.list_display)
        return u'%s\n%s\n%s' % (unicode(self.student), unicode(self.term),
                                class_list)
