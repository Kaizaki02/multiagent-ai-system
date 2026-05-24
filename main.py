from src.tools.tools import web_search,scrape_url

# print(web_search("What is the latest news on AI?"))
results = scrape_url.invoke("https://www.reddit.com/r/AISEOInsider/comments/1rs1o1v/latest_ai_news_the_biggest_ai_announcements_right")
print(results)


