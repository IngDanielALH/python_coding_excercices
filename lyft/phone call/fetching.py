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

MAX_RESULTS = 103
PAGE_SIZE = 1


class FetchPageResult(TypedDict):
    next_page: int | None
    results: list[int]

    # External API -- Should not be modified for solution


def fetch_page(page: int) -> FetchPageResult:
    """
    Return the page of results and the next page. Pages are 0 indexed.
    returns:
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


class ResultFetcher:

    def __init__(self) -> None:
        pass

    def fetch(self, num_results: int, start_page: int) -> list[int]:
        results = []
        for num in range(start_page, start_page + num_results):
            page_data = fetch_page(num)  # Llamada a la API paginada
            if page_data['results']:  # Verifica si la lista no está vacía
                results.append(page_data['results'][0])
        return results
