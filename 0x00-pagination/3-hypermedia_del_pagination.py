#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initializes server instance.
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns a paginated set of data from the server without missing
        items when page changes.

        Args:
            index (int): Current start index of returning page.
            page_size (int): Size of the page returned.

        Returns:
            (Dict): Containing data page and some metadata.
        """
        indexed_dataset = self.__indexed_dataset

        # Index and page size arguments validation
        assert isinstance(index, int)
        assert index >= 0 and index < len(indexed_dataset)
        assert isinstance(page_size, int) and page_size > 0

        # Load indexed data
        self.indexed_dataset()

        # Get data within specified range
        start = index
        end = index + page_size
        data = []
        indexes = []  # Store indexes of data retrieved here
        for i in range(start, end, 1):
            if i in indexed_dataset:
                data.append(indexed_dataset[i])
                indexes.append(i)

        # Get start index for next page (next_index)
        next_index = indexes[-1] + 1
        # Loop until next valid index is found
        while not indexed_dataset.get(next_index):
            if next_index == len(indexed_dataset):
                next_index = -1
                break
            next_index += 1

        result = {
                "index": indexes[0],
                "next_index": next_index,
                "page_size": len(data),
                "data": data
                }

        return result
