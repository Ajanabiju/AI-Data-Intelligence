from crawlers.arxiv_scraper import get_recent_papers
from crawlers.job_scraper import get_jobs
from crawlers.news_scraper import get_news

from exporters.csv_exporter import export_to_csv
from exporters.jobs_exporter import export_jobs
from exporters.news_exporter import export_news

print("\nCollecting Research Papers...")
papers = get_recent_papers(20)

print("Collecting Jobs...")
jobs = get_jobs()

print("Collecting News...")
news = get_news()

# Export Papers
export_to_csv(
    papers,
    "../output/research_papers.csv"
)

# Export Jobs
export_jobs(
    jobs,
    "../output/jobs.csv"
)

# Export News
export_news(
    news,
    "../output/news.csv"
)

print("\nPipeline Completed Successfully!")

print(f"Papers: {len(papers)}")
print(f"Jobs: {len(jobs)}")
print(f"News: {len(news)}")