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
        assert isinstance(index, int) and index < len(self.__indexed_dataset)
        assert isinstance(page_size, int) and page_size > 0

        # Load file into cache
        self.dataset()
        self.indexed_dataset()

        # Get dataset within specified range
        data = []
        start = index
        end = index + page_size
        for i in range(start, end, 1):
            if i in self.__indexed_dataset:
                row = self.__indexed_dataset.get(i)
                data.append(row)

        # Compute metadata
        page_size = len(data)
        index = 
        next_index = end + 1
        while not self.__indexed_dataset.get(next_index):
            next_index += 1

        result = {
                "index": sorted(data)[0],
                "next_index": next_index,
                "page_size": page_size,
                "data": data
                }

        return result
