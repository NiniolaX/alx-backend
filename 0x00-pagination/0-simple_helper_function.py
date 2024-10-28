#!/usr/bin/env python3
"""
Contains a simple helper function for calculating the index range for
pagination of a data set
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Returns a tuple containing the start and end indexes to return in a list.

    Args:
        page(int): Page.
        page_size: Number of items each page should contain.

    Return:
        (tuple): start and end indexes to return in list of items.
    """
    if not page or not isinstance(page, int):
        return
    if not page_size or not isinstance(page_size, int):
        return

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
