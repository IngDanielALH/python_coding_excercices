"""
Paginated API

Problem Description

A third-party API that we're using has a paginated API. It returns results in chunks of N. This is implemented below on
"fetch_page".

We don't think that API is very useful, and would prefer the following implementation where only one call to "fetch"
will return a given number of results, abstracting away the need to do pagination.

Your task will be to implement ResultFetcher.fetch()
"""
from __future__ import annotations
from typing import TypedDict


# These numbers are for testing only and may be changed by the interviewer.
# Do not use them in your solution

MAX_RESULTS = 103
PAGE_SIZE = 1

class FetchPageResult(TypedDict):
    next_page: int | None
    results: list[int]

# External API -- Should not be modified for solution
def fetch_page(page: int) -> FetchPageResult:
    """
    Return the page of results and the next page. Pages are 0 indexed.

    Returns:
    {
        "results": [...],
        "next_page": 3
    }
    """
    if page * PAGE_SIZE > MAX_RESULTS:
        return {"next_page": None, "results": []}

    return {
        "next_page": page + 1,
        "results": list(
            range(page * PAGE_SIZE, min(MAX_RESULTS, (page + 1) * PAGE_SIZE))
        ),
    }

################ Implement Solution here ################

class ResultFetcher:
    def __init__(self) -> None:
        pass

    def fetch(self, num_results: int) -> list[int]:
        results = []
        return results
