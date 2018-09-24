""" faketraffic.py
    Usage:
        faketraffic.py <url-list> <time1> <time2> 
        faketraffic.py <url-list> <time>
        faketraffic.py -h | --help

    Options:
        -h, --help  :   show this help message
        url-list    :   .txt-file containing comma-separated urls. has to be in the same path
        time        :   static time period within the requests are send (seconds)
        time1,time2 :   requests are send within random generated period of times between the two given (seconds)

"""
import requests
import csv
from docopt import docopt
import random
from time import sleep



def check_internet_connection():
    """
    Trying to connect to google for checking if internet is available
    :return: True if succeed, false if fails
    """
    url = 'http://www.google.com'
    timeout = 1
    try:
        requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False


def make_url_list(filename):
    """
    Generating a list of urls by iterating through the csv-document named in the argument
    :param filename: name of the textfile which contains the comma separated values (csv)
    :return: python list of the values
    """
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        url_list = []
        for element in csv_reader:
            url_list = element
        print url_list
        return url_list


def send_requests(url_list, time1, time2):
    """
    Sending requests to randomly chosen urls in the url_list by using randomized index-variables. After each request
    going to sleep for a static or random amount of time
    :param url_list: list of urls returned by make_url_list
    :param time1: random time between time1-time2
    :param time2: random time between time1-time2
    :return:
    """
    while (True):
        requests.get(url_list[random.randint(0, (len(url_list) - 1))])
        print random.randint(int(time1), int(time2))
        sleep(random.randint(int(time1), int(time2)))


def main(docopt_args):
    if (check_internet_connection() == True):
        url_list = docopt_args["<url-list>"]
        if docopt_args["<time>"]:
            time1 = docopt_args["<time>"]
            time2 = time1
        else:
            time1 = docopt_args["<time1>"]
            time2 = docopt_args["<time2>"]

        url_list = make_url_list(url_list)
        send_requests(url_list, time1, time2)
    else:
        print "no internet connection"


if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)
