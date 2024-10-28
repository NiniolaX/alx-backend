#!/usr/bin/env python3
"""
Contains a simple helper function for calculating the index range for
pagination of a data set
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing the start and end indexes to return in a list
    for pagination.

    Args:
        page(int): Page.
        page_size: Number of items each page should contain.

    Returns:
        (Tuple[int, int]): start and end indexes to return in list for
        pagination.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
