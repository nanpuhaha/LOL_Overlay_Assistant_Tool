from scrapy import cmdline

cmdline.execute('scrapy crawl champion_spider -o ../results/champion.json'.split())


# cmdline.execute('scrapy crawl item_spider -o ../results/items.csv'.split())
