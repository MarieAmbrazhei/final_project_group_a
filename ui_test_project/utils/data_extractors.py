from typing import Union, List, Any


class DataExtractor:

    @staticmethod
    def extract_value_by_key(
            data: Union[dict, list],
            key: str,
            find_all: bool = False
    ) -> Union[Any, List[Any], None]:
        """Recursively searches for a value by the given key in a dictionary
        or list with arbitrary nesting. Returns either the first match or all matches
        depending on the `find_all` flag.
        """
        results = []

        def recursive_search(data: Union[dict, list]):
            if isinstance(data, dict):
                for k, v in data.items():
                    if k == key:
                        if find_all:
                            results.append(v)
                        else:
                            return v
                    if isinstance(v, (dict, list)):
                        result = recursive_search(v)
                        if result is not None and not find_all:
                            return result
            elif isinstance(data, list):
                for item in data:
                    result = recursive_search(item)
                    if result is not None and not find_all:
                        return result
            return None

        result = recursive_search(data)
        return results if find_all else result

    @staticmethod
    def extract_objects_by_value(
            data: Union[dict, list],
            target_value: Any,
            find_all: bool = False
    ) -> Union[dict, list, None]:
        """
        Recursively searches for the target value in a dictionary or list
        with arbitrary nesting.

        Args:
            data (Union[dict, list]): The dictionary or list to search within.
            target_value (Any): The value to search for.
            find_all (bool, optional): If True, returns all matching objects.
            If False, returns the first match. Defaults to False.

        Returns:
            Union[dict, list, None]: A list of matching objects if `find_all` is True and matches are found,
                                     a single matching object if `find_all` is False and a match is found,
                                     or None if no matches are found.
        """
        results = []

        def recursive_search(data):
            if isinstance(data, dict):
                for key, value in data.items():
                    if value == target_value:
                        results.append(data)
                        if not find_all:
                            return True
                    elif isinstance(value, (dict, list)):
                        if recursive_search(value) and not find_all:
                            return True
            elif isinstance(data, list):
                for item in data:
                    if recursive_search(item) and not find_all:
                        return True

        recursive_search(data)
        return results if results else None
