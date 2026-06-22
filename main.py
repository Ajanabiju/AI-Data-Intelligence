from crawlers.news_scraper import get_ai_news

articles = get_ai_news()

print(
    f"\nFound {len(articles)} news articles\n"
)

for article in articles:

    print("-" * 50)

    print(article["title"])

    print(article["published"])

    print(article["url"])