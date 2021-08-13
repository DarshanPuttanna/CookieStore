import unittest
import mostVisitedCookie

from pathlib import Path
from unittest.mock import patch


from cookieStore import CookieStore, DateStore
from io import StringIO


class TestMostVisitedCookie(unittest.TestCase):
    def setUp(self) -> None:
        self.testCookieList = [['AtY0laUfhglK3lC7', '2018-12-09'],
                               ['AtY0laUfhglK3lC7', '2018-12-09'],
                               ['SAZuXPGUrfbcn5UA', '2018-12-09'],
                               ['SAZuXPGUrfbcn5UA', '2018-12-09'],
                               ['SAZuXPGUrfbcn5UA', '2018-12-09'],
                               ['5UAVanZf6UtGyKVS', '2018-12-09'],
                               ['AtY0laUfhglK3lC7', '2018-12-09'],
                               ['SAZuXPGUrfbcn5UA', '2018-12-08'],
                               ['4sMM2LxV07bPJzwf', '2018-12-08'],
                               ['fbcn5UAVanZf6UtG', '2018-12-08'],
                               ['4sMM2LxV07bPJzwf', '2018-12-07'],
                               ['4sMM2LxV07bPJzwf', '2018-12-07']]

    def test_get_first_index_for_date(self):
        query_date = '2018-12-07'
        self.assertEqual(10, mostVisitedCookie.get_first_index_for_date(self.testCookieList, query_date))

    def test_process_cookie_search_with_invalid_file(self):
        query_date = '2018-12-07'
        file_name = 'test.csv'
        with patch.object(Path, 'exists') as mock_exists:
            mock_exists.return_value = False
            with self.assertRaises(Exception) as exception_context:
                mostVisitedCookie.process_cookie_search(file_name, query_date)
            self.assertEqual('File not found. Please pass a valid csv file to process',
                             str(exception_context.exception))

    def test_process_cookie_search_with_empty_file(self):
        query_date = '2018-12-07'
        file_name = 'test.csv'
        mock_data = ''
        with patch.object(Path, 'exists') as mock_exists:
            mock_exists.return_value = True
            mock_open_object = unittest.mock.mock_open(read_data=mock_data)
            with patch('builtins.open', mock_open_object):
                mock_open_object.return_value = StringIO(mock_data)
                with self.assertRaises(Exception) as exception_context:
                    mostVisitedCookie.process_cookie_search(file_name, query_date)
                self.assertEqual('No data to process', str(exception_context.exception))

    def test_get_most_visited_cookie_for_date(self):
        query_date = '2018-12-07'
        file_name = 'test.csv'
        mock_data = '4sMM2LxV07bPJzwf, 2018-12-07'
        with patch.object(Path, 'exists') as mock_exists:
            mock_exists.return_value = True
            mock_open_object = unittest.mock.mock_open(read_data=mock_data)
            with patch('builtins.open', mock_open_object):
                mock_open_object.return_value = StringIO(mock_data)
                self.assertEqual(['4sMM2LxV07bPJzwf'], mostVisitedCookie.process_cookie_search(file_name, query_date))


class TestCookieStore(unittest.TestCase):
    def setUp(self) -> None:
        self.testCookieList = [['4sMM2LxV07bPJzwf', '2018-12-07'],
                               ['4sMM2LxV07bPJzwf', '2018-12-07']]

    def test_write_cookie_id_for_given_date(self):
        test_curr_date = '2018-12-07'
        test_cookie_id = 'testcookieid'
        test_cookie_store = CookieStore()
        with patch('cookieStore.DateStore') as mock_datestore:
            mock_instance = mock_datestore.return_value
            test_cookie_store.write_cookie_id_to_cookie_store(test_curr_date, test_cookie_id)
            mock_datestore.assert_called_once_with(test_curr_date)
            mock_instance.update_cookie_count.assert_called_once_with(test_cookie_id)

    def test_get_most_visited_cookie_for_given_date(self):
        test_curr_date = '2018-12-07'
        test_cookie_id = 'testcookieid'
        test_cookie_store = CookieStore()
        with patch('cookieStore.DateStore') as mock_datestore:
            mock_instance = mock_datestore.return_value
            test_cookie_store.dateVisited[test_curr_date] = mock_instance
            test_cookie_store.get_most_visited_cookie_for_given_date(test_curr_date)
            mock_instance.most_visited_cookie.assert_called_once_with()


class TestDate(unittest.TestCase):
    def setUp(self) -> None:
        self.test_cookie_data = {'AtY0laUfhglK3lC7': 3, 'SAZuXPGUrfbcn5UA': 1, '5UAVanZf6UtGyKVS': 3,
                                 'AtY0laUfhglK3lC9': 2}
        self.test_date_store = DateStore('test_date')
        self.test_date_store.cookieData = self.test_cookie_data

    def test_most_visited_cookie(self):
        expected_cookie_list = ['AtY0laUfhglK3lC7', '5UAVanZf6UtGyKVS']
        self.assertEqual(expected_cookie_list, self.test_date_store.most_visited_cookie())

    def test_update_cookie_count_for_new_cookie_id(self):
        test_new_cookie_id = 'testnewcookieid'
        self.test_date_store.update_cookie_count(test_new_cookie_id)
        expected_cookie_count = 1
        self.assertEqual(expected_cookie_count, self.test_date_store.cookieData.get(test_new_cookie_id))

    def test_update_cookie_count_for_existing_cookie_id(self):
        test_existing_cookie_id = 'SAZuXPGUrfbcn5UA'
        self.test_date_store.update_cookie_count(test_existing_cookie_id)
        expected_cookie_count = 2
        self.assertEqual(expected_cookie_count, self.test_date_store.cookieData.get(test_existing_cookie_id))


if __name__ == '__main__':
    unittest.main()
