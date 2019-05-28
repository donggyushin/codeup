year, month, day = input().split('.')
mon_len = len(month)
day_len = len(day)
year_len = len(year)
if mon_len == 1:
    month = '0'+month
if day_len == 1:
    day = '0'+day
if year_len == 1:
    year = '000'+year
elif year_len == 2:
    year = '00'+year
elif year_len == 3:
    year = '0'+year
print(year+'.'+month+'.'+day)
