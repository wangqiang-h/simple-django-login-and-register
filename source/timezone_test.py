import pytz
import datetime


def change_local_to_utc(t):
    import pytz
    import datetime

    t_format = "%Y-%m-%d %H:%M:%S"
    t_timezone = "Asia/Shanghai"
    local = pytz.timezone(t_timezone)
    naive = datetime.datetime.strptime(t, t_format)
    local_dt = local.localize(naive, is_dst=None)
    utc_dt = local_dt.astimezone(pytz.utc)
    return utc_dt


t = change_local_to_utc("2020-11-30 05:11:12")


def local_t(t):
    from datetime import datetime
    return datetime.strptime(t, '%Y-%m-%d %H:%M:%S')


from dbmodels.models import Student
from django.utils import timezone

s = Student.objects.create(name="wq", age=10, birthday=timezone.now())
print(s.birthday)
# print(Student.objects.filter(birthday__gt=change_local_to_utc("2020-11-30 11:13:12")))

print(Student.objects.filter(birthday__gt=local_t("2020-11-30 11:13:12")))
