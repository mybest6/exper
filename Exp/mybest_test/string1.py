# encoding:utf-8
# str1 = 'https://so.haodf.com/index/search?kw='
# str2 = '&page='
# with open('dingx.txt', 'r+') as f:
#   for line in f.readlines():
#     line = line.strip()
#     for i in range(1,101):
#         a = str1 + line+ str2 + str(i)
#         f.write(a)
#         f.write('\n')
# 'https://pubmed.ncbi.nlm.nih.gov/'+'?term='
# https://so.haodf.com/index/search?kw=%B8%DF%D1%AA%D1%B9&page=1
# http://so.qiuyi.cn/search.php?q=%E9%AB%98%E8%A1%80%E5%8E%8B&m=&f=_all&s=&p=4&rank=question
# https://so.haodf.com/index/search?kw=%E9%AB%98%E8%A1%80%E5%8E%8B&page=3
# https://so.haodf.com/index/search?kw=%E9%AB%98%E8%A1%80%E5%8E%8B&page=2
# https://www.chunyuyisheng.com/pc/search/qalist/?query=高血压&page=1
# http://wapask.9939.com/hot/sd/高血压/1#kwd=高血压
# http://wapask.9939.com/hot/sd/高血压/2#kwd=高血压
# http://wapask.9939.com/hot/sd/高血压/3#kwd=高血压
# https://so.familydoctor.com.cn/search?t=ask&q=高血压&page=1&
#https://www.chunyuyisheng.com/pc/search/qalist/?query=高血压&page=1
# https://dxy.com/questions/60?tag_id=11091&page_index=1
# http://so.39.net/search/wd?words=%e7%b3%96%e5%b0%bf%e7%97%85%20%e8%a1%80%e7%b3%96&start=1
# http://so.fh21.com.cn/?kw=%E9%AB%98%E8%A1%80%E5%8E%8B&type=question&page=2
# http://zhannei.baidu.com/cse/search?q=%E9%AB%98%E8%A1%80%E5%8E%8B&p=2&s=10648517351426963974&entry=1
# http://wapask.9939.com/hot/sd/%E9%AB%98%E8%A1%80%E5%8E%8B/2
# https://www.chunyuyisheng.com/pc/search/qalist/?query=%E9%AB%98%E8%A1%80%E5%8E%8B&page=1
# https://so.familydoctor.com.cn/search?t=ask&q=%e9%ab%98%e8%a1%80%e5%8e%8b&page=2&
# https://so.99.com.cn/search.php?q=%E9%AB%98%E8%A1%80%E5%8E%8B&m=&f=_all&s=relevance&p=3&proj=qwask
# http://so.xywy.com/wenda.php?keyword=%E9%AB%98%E8%A1%80%E5%8E%8B&src=so&page=3
# http://so.xywy.com/comse.php?keyword=%E9%AB%98%E8%A1%80%E5%8E%8B&page=3&src=so

# http://so.120ask.com/?kw=%E9%AB%98%E8%A1%80%E5%8E%8B&page=2&isloc=1

str1 = 'https://pubmed.ncbi.nlm.nih.gov/?term='
with open('dingx.txt', 'r+') as f:
  for line in f.readlines():
    line = line.strip()
    a = str1 + line
    f.write(a)
    f.write('\n')

# 'https://pubmed.ncbi.nlm.nih.gov/'+'?term='
# http://so.xywy.com/wenda.php?keyword=高血压&src=so&page1
# http://zhannei.baidu.com/cse/search?q=%E9%AB%98%E8%A1%80%E5%8E%8B&p=1&s=10648517351426963974&entry=1
# https://so.99.com.cn/search.php?q=%E9%AB%98%E8%A1%80%E5%8E%8B&m=&f=_all&s=relevance&p=1&proj=qwask
# https://so.99.com.cn/search.php?q=%E9%AB%98%E8%A1%80%E5%8E%8B&m=&f=_all&s=relevance&p=3&proj=qwask
# str1 = '#kwd=糖尿病'
# with open('dingx.txt', 'r+') as f:
#   for line in f.readlines():
#       # for i in range(1,11):
#         line = line.strip()
#         a =  line+ str1
#         f.write(a)
#         f.write('\n')
#

# http://so.39.net/search/wd?words=%e7%b3%96%e5%b0%bf%e7%97%85%20%e8%a1%80%e7%b3%96&start=1
# http://wapask.9939.com/hot/sd/%E7%B3%96%E5%B0%BF%E7%97%85%20+%20%E8%A1%80%E7%B3%96/1
# http://zhannei.baidu.com/cse/search?q=%E8%A1%80%E7%B3%96%20%E9%AB%98%E8%A1%80%E5%8E%8B&p=0&s=10648517351426963974&entry=1
# http://so.39.net/search/wd?words=糖尿病 血糖&start=1
# https://so.familydoctor.com.cn/search?t=ask&q=%e7%b3%96%e5%b0%bf%e7%97%85+%e8%a1%80%e7%b3%96&page=3&
# http://so.120ask.com/?kw=%E7%B3%96%E5%B0%BF%E7%97%85%20%E9%AB%98%E8%A1%80%E5%8E%8B&page=3&isloc=1
# http://so.39.net/search/s?words=%E7%B3%96%E5%B0%BF%E7%97%85%20%E8%A1%80%E7%B3%96&start=1
# http://so.39.net/search/wd?words=%E7%B3%96%E5%B0%BF%E7%97%85%20%E8%A1%80%E7%B3%96&start=3
# http://so.xywy.com/wenda.php?keyword=%E7%B3%96%E5%B0%BF%E7%97%85+%E8%A1%80%E7%B3%96&src=so&page=1
# http://so.qiuyi.cn/search.php?q=%E7%B3%96%E5%B0%BF%E7%97%85%20%E8%A1%80%E7%B3%96&m=&f=_all&s=&p=1&rank=question
# http://so.qiuyi.cn/search.php?q=糖尿病 血糖&m=&f=_all&s=&p=60&rank=question
# http://so.fh21.com.cn/?kw=%E7%B3%96%E5%B0%BF%E7%97%85+%E8%A1%80%E7%B3%96&type=question&page=1
# http://so.fh21.com.cn/?kw=三高 血糖&type=question&page=1
# http://so.fh21.com.cn/?kw=%E7%B3%96%E5%B0%BF%E7%97%85%20%E8%A1%80%E7%B3%96&type=question&page=2