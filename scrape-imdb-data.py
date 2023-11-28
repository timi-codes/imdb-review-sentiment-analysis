import scrapy
import json

class IMDbReviewsSpider(scrapy.Spider):
    name = "review_spider"

    def start_requests(self):
        yield scrapy.Request("The Godfather", callback=self.parse, meta={"title": "https://www.imdb.com/title/tt0068646/reviews?ref_=tt_urv"})

    def parse(self, response):
        title = response.meta["title"]
        print(title)
        # Extracting review details
        review_blocks = response.css("div.lister-item-content")

        for block in review_blocks:
            review = block.css("div.text.show-more__control::text").get()

            # Creating a dictionary for the extracted data
            review_data = {
                "title": title,
                "review": review
            }
            print(review_data)
            # Yielding the extracted data
            yield review_data

        # Follow pagination link if available
        next_page_url = response.css("a.lister-page-next::attr(href)").get()
        if next_page_url:
            yield response.follow(next_page_url, self.parse, meta={"title": title})


data = IMDbReviewsSpider()
review = data.start_requests()
print(review)
