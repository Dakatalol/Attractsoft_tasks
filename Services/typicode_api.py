from Utils.api_utility import ApiInteractions


class typicodeAPI:
    """
    This class allows the user to hit the various endpoints that are accessible in the service
    and returns the response back to be used to validate the responses.
    """
    base_url = f'https://jsonplaceholder.typicode.com/'
    auth = None
    headers = {'Content-Type': 'application/json'}

    # GET Requests
    @classmethod
    def get_blog_posts(cls,):
        """
        Returns a list of blog posts if blog number is not filled
        If blog_number is filled returns the specific blog_id result
        """
        return ApiInteractions.get(cls.base_url + 'posts/', header_data=cls.headers)
