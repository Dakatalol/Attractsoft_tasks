from Utils.api_utility import ApiInteractions


class TypicodeAPI:
    """
    This class allows the user to hit the various endpoints that are accessible in the service
    and returns the response back to be used to validate the responses.
    """
    base_url = f'https://jsonplaceholder.typicode.com/'
    auth = None
    headers = {'Content-Type': 'application/json'}

    # GET Requests
    @classmethod
    def get_blog_posts(cls, ):
        """
        Returns a list of blog posts
        """
        return ApiInteractions.get(cls.base_url + 'posts/', header_data=cls.headers)
