class CookieStore:

    def __init__(self):
        self.dateVisited = {}

    def write_cookie_id_to_cookie_store(self, curr_date, cookie_id):
        """ Writes the processed data into cookie store. """
        if curr_date not in self.dateVisited:
            curr_date_store = DateStore(curr_date)
            self.dateVisited[curr_date] = curr_date_store

        self.dateVisited[curr_date].update_cookie_count(cookie_id)

    def get_most_visited_cookie_for_given_date(self, query_date):
        """ Fetch the list of most visited cookies for a given query date. """
        if query_date in self.dateVisited:
            return self.dateVisited[query_date].most_visited_cookie()


class DateStore:

    def __init__(self, curr_date):
        self.currDate = curr_date
        self.cookieData = {}

    def update_cookie_count(self, cookie_id):
        """ Create/Update the cookie_id and count in cookieData dictionary. """
        self.cookieData[cookie_id] = self.cookieData.get(cookie_id, 0) + 1

    def most_visited_cookie(self):
        """Creates the list of all cookies with maximum number of counts from cookieData dictionary. """
        cookie_list = []
        max_cookie_count = 0
        for cookie_id, cookie_count in self.cookieData.items():
            if cookie_count > max_cookie_count:
                max_cookie_count = cookie_count
                cookie_list = [cookie_id]
            elif cookie_count == max_cookie_count:
                cookie_list.append(cookie_id)
        return cookie_list
