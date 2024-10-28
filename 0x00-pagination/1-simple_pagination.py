#!/usr/bin/env python3
"""
Performs simple pagination on a dataset
"""
import csv
import math
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a list of data (page) from a range of specified values

        Args:
            page: Data items to return.
            page_size: Number of items each page would display.

        Returns:
            List of Lists: List of rows of data to represent page.

        Raises:
            AssertionError: If page or page_size is not greater than 0.
        """
        # Raise AssertionError if page or page_size are not positive integers
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Get range of dataset to return
        start, end = index_range(page, page_size)

        # Load file into cache
        self.dataset()

        # Return empty list if CSV file contains no data
        if not self.dataset():
            return []

        # Return empty list if input arguments are out of range for dataset
        if end > len(self.__dataset):
            return []

        return self.__dataset[start:end]
