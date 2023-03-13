import requests


class ApiInteractions:
    """
    Helper utility for making CRUD operations on end points. Works with no auth, OAuth1 and Basic Auth.
    """

    @classmethod
    def get(cls, url: str, header_data: dict = None, allow_redirects: bool = True):
        """
        Perform a GET request
        Args:
            url: Endpoint URL
            header_data: JSON formatted Headers for the request
            allow_redirects: Override if you want to prevent any redirects from occurring
        Returns:
            Response data from the request
        """
        return requests.get(url, headers=header_data, allow_redirects=allow_redirects)
