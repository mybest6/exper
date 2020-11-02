#encoding:utf-8
# s = '2018年6月12日 09:06'
# def process(s):
#     import time
#     year = s.split("年")[0]
#     month = s.split("年")[1].split("月")[0]
#     day = s.split("年")[1].split("月")[1].split("日")[0]
#     last = s.split(" ")[-1].strip()
#     a = "{}-{}-{} {}:00".format(year,month,day,last)
#     create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(a,"%Y-%m-%d %H:%M:%S"))
#     return create_time
# print(process(s))

def process(s):
    import time
    a = "{}:00".format(s)
    create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(a,"%Y-%m-%d %H:%M:%S"))
    return create_time
print(process('2015-01-15 02:36'))