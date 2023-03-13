class JsonUtil:

    @classmethod
    def sum_blog_posts_per_user(cls, userid, json):
        user_count_dict = {}
        counter = 0
        for item in json:
            if item['userId'] == userid:
                counter += 1
        user_count_dict[userid] = counter
        return user_count_dict

    @classmethod
    def find_blog_by_number_for_specific_user(cls, userid, blog_number, json):
        counter = 0
        for item in json:
            if item['userId'] == userid:
                counter += 1
                if blog_number == counter:
                    return item['id']
