from Utils.ui_utility import ElementInteractions, BrowserInteractions, ElementWait
import time


class AmazonPage:
    """Xpath selectors and methods for the main amazon page"""

    # Xpath Selectors

    # text boxes
    amazon_search_field = "//input[@id='twotabsearchtextbox']"

    # text fields
    deal_text = "//span[contains(@class, 'savingsPercentage')]"
    save_text = "//td[.='  You Save: ']"
    cart_subtotal = "//div[@id='attachDisplayAddBaseAlert']//h4[@class='a-alert-heading']"
    product_title_text = "//span[@id='productTitle']"
    cart_product_titles = "//ul/li[@class='a-spacing-mini']"
    shop_by_department_title_text = "//div[@id='hmenu-content']/ul[@class='hmenu hmenu-visible']/li[6]"
    category_names = "//ul[@class='hmenu hmenu-visible hmenu-translateX']//li/a"

    # buttons/links
    amazon_search_button = "//input[@id='nav-search-submit-button']"
    amazon_item_links = "//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']"
    add_to_cart_button = "//input[contains(@id, 'add-to-cart-button')]"
    check_out_button = "//span[@id='sc-buy-box-ptc-button']//input[@name='proceedToRetailCheckout']"
    cart_button = "//a[@id='nav-cart']"
    all_hamburger_button = "//a[@id='nav-hamburger-menu']"
    see_all_button = "//div[@id='hmenu-content']/ul[@class='hmenu hmenu-visible']/li[11]/a[1]"

    # select-menu
    departament_select_menu = "#searchDropdownBox"
    departament_names_option = "//select[@id='searchDropdownBox']/option"

    @classmethod
    def search_for_item(cls, text):
        ElementInteractions.enter_text(cls.amazon_search_field, text)
        ElementInteractions.click(cls.amazon_search_button)

    @classmethod
    def get_all_links(cls):
        links = []
        # gets all links that are present on the search page
        for item in ElementInteractions.get_attribute(cls.amazon_item_links, attribute='href', get_all=True):
            links.append(item)
        # returns all unique links as a list
        return list(set(links))

    @classmethod
    def add_all_not_discounted_items_to_cart(cls, url_list):
        added_products = []
        for link in url_list:
            # navigates to the product page
            BrowserInteractions.go_to_url(link)
            # gets the product title
            title = ElementInteractions.get_text(cls.product_title_text)
            # checking if the product is not discounted
            if not ElementInteractions.is_displayed(cls.deal_text) and not ElementInteractions.is_displayed(
                    cls.save_text):
                try:
                    # adding the product in the basket
                    ElementInteractions.click(cls.add_to_cart_button)
                    added_products.append(title)
                    ElementWait.wait_for_element_to_appear(cls.cart_subtotal)
                except:
                    pass
        return list(set(added_products))

    @classmethod
    def go_to_cart(cls):
        BrowserInteractions.go_to_url(ElementInteractions.get_attribute(cls.cart_button, attribute='href'))
        ElementWait.wait_for_element_to_be_clickable(cls.check_out_button)

    @classmethod
    def get_all_items_in_cart(cls):
        return ElementInteractions.get_text(cls.cart_product_titles, get_all=True)

    @classmethod
    def compare_two_lists(cls, expected, actual):
        """
        returns boolean if two lists are equal
        """
        if len(expected) != len(actual):
            return False
        return expected.sort() == actual.sort()

    @classmethod
    def crawl_departament_links(cls):
        departament_urls = []
        ElementInteractions.click(cls.departament_select_menu)
        # getting all menu option values and building the proper urls
        for url in ElementInteractions.get_attribute(cls.departament_names_option, attribute='value', get_all=True):
            url = "https://www.amazon.com/s/ref=nb_sb_noss?url=" + url
            departament_urls.append(url)
        # we don't need this, it's the default drop option
        departament_urls.pop(0)
        # opening the file for writing with datetime.now() timestamp as name
        # the file saves in project /tests folder
        with open(f"{time.time()}.txt", "w") as text_file:
            for url in departament_urls:
                BrowserInteractions.go_to_url(url)
                # verify if the page loads successfully
                if ElementInteractions.execute_script('return document.readyState') == 'complete':
                    status = 'OK'
                else:
                    status = 'DeadLink'
                title = BrowserInteractions.get_title()
                text_file.write(f"link:{url}, page title: {title}, status: {status}\n")
