from scrapy import cmdline
cmdline.execute("scrapy crawl myspider -o info.csv".split())
