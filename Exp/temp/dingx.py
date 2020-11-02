# -*- encoding: utf8 -*-
import json
import re
from elasticsearch import Elasticsearch
from elasticsearch import helpers

ELASTICSEARCH_THRIFT_IP_AND_PORT_LIST = ['http://192.168.100.225:9200',
                                         'http://192.168.100.226:9200',
                                         'http://192.168.100.227:9200']


class ESSrcPages(object):
    def __init__(self):
        # the default port is 9200
        self.reconnect()

    def reconnect(self):
        self.es = Elasticsearch(ELASTICSEARCH_THRIFT_IP_AND_PORT_LIST,
                                sniff_on_start=True,
                                sniff_on_connection_fail=True,
                                sniffer_timeout=60, timeout=5000, sniff_timeout=5)

    def get_by_query(self, ):
        query = {
            "query": {
                "term": {
                    "taskId": {
                        "value": "5dae58d97cf595c8ab4c62c5b34c86b1"
                    }
                }
            }
        }
        f = open('./abc.txt','w',encoding='utf-8')
        unq = set()
        results = helpers.scan(
                self.es,
                index="crawler_response",
                doc_type='hbase_log',
                query=query,
                preserve_order=False,
                scroll="30m",
                size=500,
                timeout="30m")
        for result in results:
            try:
                body = result.get("_source").get("body")
                kwd_str = result.get("_source").get("oracle")
                kwd_dic = json.loads(kwd_str)
                kwd = kwd_dic.get(u"kwd")
                body_s = re.findall('"items":(.+?)},"hotSearchTags"',body,re.S)
                a_s= body_s[0]
                # a = a_s.split(";")[0]
                # https://dxy.com/question/70746984
                body_dict = json.loads(a_s)
                for i in body_dict:
                    if i.get("id") not in unq:
                        f.write("https://dxy.com/question/{}\n".format(i.get("id")))
                        unq.add(i.get("url"))
            except Exception as e:
                print(e)
            # items_list = body_dict.get("items")
            # for item in items_list:


if __name__ == '__main__':
    essrcpages = ESSrcPages()
    essrcpages.get_by_query()
    # # results = es.get_pages_by_sid('695')
    # # uid = '17ba1dc5fe7edf95833349401f473ac2'
    # results = essrcpages.es.search(index="map_project", body={'query': {'match': {'name': '杭州费尔斯通科技有限公司'}}})
    # i = 0
    # print results
