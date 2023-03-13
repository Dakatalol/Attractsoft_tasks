import pytest

from Pages.amazon.amazon_page import AmazonPage


@pytest.mark.smoke
def test_amazon_laptop_task():
    """
    GIVEN user is navigated to the amazon webpage successfully
    WHEN the user searches for laptops
    AND the user adds all the laptops(non-discounted and in stock) from the first page of the search result
    AND the user navigates to the shopping cart
    THEN the user is able to see that all the added laptops from before are visible in the cart
    """
    # searching for 'laptop'
    AmazonPage.search_for_item("laptop")
    # adding all not discounted items to the cart by getting all links from the search result
    added_items = AmazonPage.add_all_not_discounted_items_to_cart(AmazonPage.get_all_links())
    # navigating the to the cart page
    AmazonPage.go_to_cart()
    # getting all items in cart
    items_in_cart = AmazonPage.get_all_items_in_cart()
    # verifying that all added items are in the cart
    assert AmazonPage.compare_two_lists(items_in_cart, added_items)


@pytest.mark.smoke
def test_crawler_amazon_departments():
    """
    Crawler that opens up the “Shop By Department” dropdown menu on the amazon website,
    obtains a list of all department links and visits them to make sure that there are no dead links.
    Crawler keeps a list of visited links in a text file(/tests folder) in the form (link, page title, status),
    where status can be “OK” or “Dead link”.
    After finishing, the crawler's file name is with the following format: <timestamp>_results.txt.
    """
    AmazonPage.crawl_departament_links()
