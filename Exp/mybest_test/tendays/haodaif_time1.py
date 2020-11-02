#encoding:utf-8
def process(res):
    import re
    date = res.replace('发表于：','')
    time1 = re.findall('\d+\.\d+\.\d+', date)
    time2 = re.findall('\d+\.\d+', date)
    if time1:
        date = time1[0].replace('.', '-')
        date =  "{} 00:00:00".format(date.strip())
    elif time2:
        # replies['date'] = time.strftime("%Y")+"-"+time2[0].replace('.', '-')
        date = time.strftime("%Y")+"-"+time2[0].replace('.', '-')