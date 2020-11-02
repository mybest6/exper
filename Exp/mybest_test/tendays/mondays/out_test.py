#encoding:utf-8
def process(html):
    a = {}
    from lxml import etree
    root = etree.HTML(html, parser=etree.HTMLParser(encoding="utf-8"))
    id_list =root.xpath('//div[@class="article-page"]/@data-article-pmid')
    if id_list:
        a['id'] = 'https://pubmed.ncbi.nlm.nih.gov/'+id_list[0]
    title_list= root.xpath('//h1[@class="heading-title"]')
    if title_list:
        title = title_list[0].xpath('string(.)').strip()
        a['title'] = title
    return a