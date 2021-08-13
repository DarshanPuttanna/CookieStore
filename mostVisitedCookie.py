import csv
from cookieStore import CookieStore
import argparse
import sys
import pathlib


def get_first_index_for_date(cookie_list, req_date):
    """ Returns the first index of required date in the cookie list using binary search. """
    left = 0
    right = len(cookie_list) - 1

    result = -1
    while left <= right:
        mid = (left + right) // 2
        # if req date is located update its index
        if req_date == cookie_list[mid][1]:
            result = mid
            right = mid - 1
        # if req date is less than the middle element, discard left half
        elif req_date < cookie_list[mid][1]:
            left = mid + 1
        # if req date is greater than the middle element, discard right half
        else:
            right = mid - 1
    return result


def process_cookie_search(file_name, query_date):
    """ Fetch data from csv file from first, till last index of the query date. """
    if not pathlib.Path(file_name).exists():
        raise Exception("File not found. Please pass a valid csv file to process")
    with open(file_name) as file:
        reader = list(csv.reader(file))
        cookie_store = CookieStore()
        cookie_list = []
        if not reader:
            raise Exception('No data to process')
        for row in reader:
            curr_date = row[1].split('T')[0].strip()
            if curr_date < query_date:
                break
            cookie_id = row[0].strip()
            cookie_list.append([cookie_id, curr_date])  # listing cookie id and date

        first_index_of_required_date = get_first_index_for_date(cookie_list, query_date)

        for index in range(first_index_of_required_date, len(cookie_list)):
            cookie_id = cookie_list[index][0]
            curr_date = cookie_list[index][1]
            cookie_store.write_cookie_id_to_cookie_store(curr_date, cookie_id)

        most_visited_cookies = cookie_store.get_most_visited_cookie_for_given_date(query_date)
        return most_visited_cookies


def parse_args(args):
    """ Retrieves query date from the input command. """
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', type=str, help='query date')
    parsed_args = parser.parse_args(args)
    if parsed_args.d is None:
        raise Exception('Query date missing')
    return parsed_args


if __name__ == '__main__':
    """ Displays the most visited cookies. """
    if len(sys.argv) != 4:
        raise Exception("Invalid command. Usage $ python mostVisitedCookie.py <filename> -d <query_date>")
    filename = sys.argv[1].strip()
    date_args = parse_args(sys.argv[2:])
    most_visited_cookies = process_cookie_search(filename, date_args.d.strip())
    print('Most visited cookies are ', most_visited_cookies)
