import logging
import re
from urllib.parse import urlparse

import numpy as np
from osquery_be.extension.schemas import AnalysisVerdict
from osquery_be.settings import settings
from tld import get_tld


def have_IP(url):
    match = re.search(
        "(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\."
        "([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|"  # IPv4
        "((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)"  # IPv4 in hexadecimal
        "(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}",
        url,
    )  # Ipv6
    if match:
        return 1
    return 0


def abnormal_url(url):
    hostname = urlparse(url).hostname
    hostname = str(hostname)
    match = re.search(hostname, url)
    return 1 if match else 0


def count_dots(url):
    count_dot = url.count(".")
    return count_dot


# count the number of '@' in the URL
def count_atrate(url):
    count_atrate = url.count("@")
    return count_atrate


# count the number of '/'
def count_directory(url):
    count_dir = url.count("/")
    return count_dir


# count the number of '//'
def no_of_embed(url):
    urldir = urlparse(url).path
    return urldir.count("//")


# check if the url contains any shortnening services
def shortening_service(url):
    match = re.search(
        "bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|"
        "yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|"
        "short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|"
        "doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|"
        "db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|"
        "q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|"
        "x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|"
        "tr\.im|link\.zip\.net",
        url,
    )
    return 1 if match else 0


def count_https(url):
    return url.count("https")


def count_http(url):
    return url.count("http")


def count_per(url):
    return url.count("%")


def count_ques(url):
    return url.count("?")


def count_hyphen(url):
    return url.count("-")


def count_equal(url):
    return url.count("=")


def url_length(url):
    return len(url)


# Hostname Length
def hostname_length(url):
    return len(urlparse(url).netloc)


def suspicious_words(url):
    match = re.search(
        "PayPal|login|signin|bank|account|update|free|lucky|service|bonus|ebayisapi|webscr",
        url,
    )
    return 1 if match else 0


def digit_count(url):
    digits = 0
    digits = sum(1 for i in url if i.isnumeric())
    return digits


def letter_count(url):
    letters = 0
    letters = sum(1 for i in url if i.isalpha())
    return letters


def fd_length(url):
    urlpath = urlparse(url).path
    try:
        return len(urlpath.split("/")[1])
    except Exception as exc:
        logging.error(f"Error in fd_length: {exc}")
        return 0


def tld_length(tld):
    try:
        return len(tld)
    except Exception as exc:
        logging.error(f"Error in tld_length: {exc}")
        return -1


def preprocessed_data(url):
    status = []
    status.extend(
        [
            have_IP(url),
            abnormal_url(url),
            count_dots(url),
            count_atrate(url),
            count_directory(url),
            no_of_embed(url),
            shortening_service(url),
            count_https(url),
            count_http(url),
            count_per(url),
            count_ques(url),
            count_hyphen(url),
            count_equal(url),
            url_length(url),
            hostname_length(url),
            suspicious_words(url),
            digit_count(url),
            letter_count(url),
            fd_length(url),
        ]
    )
    tld = get_tld(url, fail_silently=True)
    status.append(tld_length(tld))
    return status


def get_prediction_from_url(test_url: str):
    features_test = preprocessed_data(test_url)
    features_test = np.array(features_test).reshape((1, -1))

    logging.debug(f"Testing: {test_url}")

    try:
        pred = settings.ml_models["url_analysis"].predict(features_test)
    except Exception as exc:
        logging.exception(f"Is the model loaded? {exc}")
        exit(1)

    res = ""
    pred_value = int(pred[0])
    if pred_value == 0:
        res = AnalysisVerdict.SAFE
    elif pred_value == 1:
        res = AnalysisVerdict.DEFACEMENT
    elif pred_value == 2:
        res = AnalysisVerdict.PHISHING
    elif pred_value == 3:
        res = AnalysisVerdict.MALWARE
    return res


if __name__ == "__main__":
    prediction = get_prediction_from_url("https://github.com/jarp0l")
    print(prediction)
