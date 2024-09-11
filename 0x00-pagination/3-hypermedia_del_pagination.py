#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed = {i: dataset[i] for i in range(len(truncated_dataset))}
        return self.__indexed

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a dictionary with pagination information
        the next index, and the actual page of the dataset.

        Args:
            index (int): The start index of the return page. Defaults to None.
            page_size (int): The number of items per page. Defaults to 10.

            Returns:
                Dict: A dictionary with pagination information.
        """
        assert index is None or 0 <= index < len(self.dataset())

        indexed_dataset = self.indexed_dataset()
        data = []
        current_index = index if index is not None else 0
        count = 0
        next_index = current_index

        while count < page_size and next_index < len(indexed_dataset):
            if next_index in indexed_dataset:
                data.append(indexed_dataset[next_index])
                count += 1
            next_index += 1

        result = {
                "index": current_index,
                "next_index": next_index,
                "page_size": page_size,
                "data": data
        }

        return result
