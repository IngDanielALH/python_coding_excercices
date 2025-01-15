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
    def __init__(self) -> None:
        pass

    def fetch(self, num_results: int) -> list[int]:
        results = []
        return results
