from crawlers.arxiv_scraper import get_recent_papers
from exporters.csv_exporter import export_to_csv

papers = get_recent_papers(20)

export_to_csv(
    papers,
    "../output/research_papers.csv"
)

print("\nExport Complete!")