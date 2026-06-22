from crawlers.startup_scraper import get_startups
from exporters.startup_exporter import export_startups

startups = get_startups(1000)

export_startups(
    startups,
    "../output/startups.csv"
)

print(
    f"\nCollected {len(startups)} startups"
)