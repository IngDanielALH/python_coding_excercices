"""
Paginated API

Problem Description

A third-party API that we're using has a paginated API. It returns results in chunks of N. This is implemented below on
"fetch_page".

We don't think that API is very useful, and would prefer the following implementation where only one call to "fetch"
will return a given number of results, abstracting away the need to do pagination.

Your task will be to implement ResultFetcher.fetch()
"""


class ResultFetcher:
    def __init__(self):
        self.current_position = 0  # Tracks the current position in the result set

    def fetch_page(self, start: int, size: int) -> list[int]:
        """Simulate fetching a page of results from a paginated API."""
        all_data = list(range(103))  # Example data, replace with actual API logic if needed
        return all_data[start:start + size]

    def fetch(self, num_results: int) -> list[int]:
        """Fetch a given number of results, abstracting away pagination."""
        results = []
        while num_results > 0:
            # Fetch results in chunks of 10 (or remaining results)
            page_size = min(10, num_results)
            page = self.fetch_page(self.current_position, page_size)
            if not page:  # If no more results are available, stop fetching
                break
            results.extend(page)
            self.current_position += len(page)  # Update position
            num_results -= len(page)  # Decrease the number of results needed
        return results
