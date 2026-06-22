from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

def is_within_24_hours(date_string):

    try:
        published = parsedate_to_datetime(date_string)

        now = datetime.now(timezone.utc)

        difference = now - published

        return difference.total_seconds() <= 86400

    except:
        return False