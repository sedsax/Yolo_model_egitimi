from icrawler.builtin import GoogleImageCrawler # type: ignore

google_crawler = GoogleImageCrawler(storage={'root_dir': 'indirilen_gorseller'})

google_crawler.crawl(keyword='kedi', max_num=30, filters={
    'type': 'photo',
    'size': 'large',
})

