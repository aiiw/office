from datetime import datetime, timedelta
# op:2开始为单体,1为双休
def get_weekend_dates(start_date_str, end_date_str,op):
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    dates = []
    n=op
    while start_date <= end_date:
        n=n+1
        # if (start_date.weekday() == 5 and n % 2 == 0) or start_date.weekday() == 6:
        if (start_date.weekday() == 5 and n % 2 == 0) :
            dates.append(start_date.strftime('%Y-%m-%d'))
        start_date += timedelta(days=1)
    return dates

#  start_date_str = input('请输入起始日期（格式为yyyy-mm-dd）：')
# end_date_str = input('请输入结束日期（格式为yyyy-mm-dd）：')
s1='2023-04-08'
s2='2023-06-14'
weekend_dates = get_weekend_dates(s1, s2,2)
print(weekend_dates)