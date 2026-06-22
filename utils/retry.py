import time
import random

def retry_request(func, max_retries=3):

    for attempt in range(max_retries):

        try:
            return func()

        except Exception as e:

            print(
                f"Attempt {attempt + 1} failed: {e}"
            )

            if attempt == max_retries - 1:
                raise

            wait_time = (
                (2 ** attempt)
                + random.uniform(0, 1)
            )

            print(
                f"Waiting {wait_time:.2f} seconds..."
            )

            time.sleep(wait_time)