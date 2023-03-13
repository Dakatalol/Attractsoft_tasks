import pytest
from Utils.json_util import JsonUtil
from Services.typicode_api import TypicodeAPI


@pytest.mark.smoke
def test_typicode_count_user_posts():
    """
    Find the count of blogs produced by a user
    Verify that user with ID=1 has 10 posts
    """
    response = TypicodeAPI.get_blog_posts()
    result = response.json()
    assert {1: 10} == JsonUtil.sum_blog_posts_per_user(1, json=result)


@pytest.mark.smoke
def test_typicode_unique_id_by_user():
    """
    Return the unique id per post from user blog list
    In example Blog with USER_ID=5 and blog_number=10 will have uniqueID = 50
    Test runs with the following data:
    (5,10), (7,10), (9,10)
    """
    response = TypicodeAPI.get_blog_posts()
    result = response.json()
    assert 50 == JsonUtil.find_blog_by_number_for_specific_user(5, 10, result) \
           and 70 == JsonUtil.find_blog_by_number_for_specific_user(7, 10, result) \
           and 90 == JsonUtil.find_blog_by_number_for_specific_user(9, 10, result)


