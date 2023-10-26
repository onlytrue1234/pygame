import time


now = time.localtime(time.time())
print(now)


year = str(now.tm_year)
month = str(now.tm_mon)
day = str(now.tm_mday)
print(year + "년" +month + "월" + day + "일")


hour = str(now.tm_hour)
minute = str(now.tm_min)
sec = str(now.tm_sec)
print(hour + "시" + minute + "분" + sec + "초")