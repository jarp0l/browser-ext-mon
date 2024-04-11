import logging
import re
from urllib.parse import urlparse

import numpy as np
from osquery_be.extension.schemas import AnalysisVerdict
from osquery_be.settings import settings
from tld import get_tld


def remove_www(url):
    url = re.sub(r"^www\.", "", url)
    return url


def length_of_url(url):
    url_length = len(url)
    return url_length


def process_tld(url):
    try:
        res = get_tld(url, as_object=True, fail_silently=False, fix_protocol=True)
        pri_domain = res.parsed_url.netloc
    except:
        pri_domain = None
    return pri_domain


def count_atrate(url):
    count_atrate = url.count("@")
    return count_atrate


def count_question(url):
    count_ques = url.count("?")
    return count_ques


def count_dash(url):
    count_dash = url.count("-")
    return count_dash


def count_equal(url):
    count_equal = url.count("=")
    return count_equal


def count_dots(url):
    count_dot = url.count(".")
    return count_dot


def count_hash(url):
    count_hash = url.count("#")
    return count_hash


def count_percent(url):
    count_percent = url.count("%")
    return count_percent


def count_plus(url):
    count_plus = url.count("+")
    return count_plus


def count_dollar(url):
    count_dollar = url.count("$")
    return count_dollar


def count_exc(url):
    count_exc = url.count("!")
    return count_exc


def count_ast(url):
    count_ast = url.count("*")
    return count_ast


def count_comma(url):
    count_comma = url.count(",")
    return count_comma


def no_of_embed(url):
    urldir = url.count("//")
    return urldir


def abnormal_url(url):
    hostname = urlparse(url).hostname
    hostname = str(hostname)
    match = re.search(hostname, url)
    return 1 if match else 0


def httpSecure(url):
    htp = urlparse(url).scheme
    match = str(htp)
    if match == "https":
        # print match.group()
        return 1
    else:
        # print 'No matching pattern found'
        return 0


def digit_count(url):
    digits = 0
    digits = sum(1 for i in url if i.isnumeric())
    return digits


def letter_count(url):
    letters = 0
    letters = sum(1 for i in url if i.isalpha())
    return letters


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


def preprocessed_data(url):
    url = re.sub(r"^www\.", "", url)
    status = []
    status.extend(
        [
            length_of_url(url),
            count_atrate(url),
            count_question(url),
            count_dash(url),
            count_equal(url),
            count_dots(url),
            count_hash(url),
            count_percent(url),
            count_plus(url),
            count_dollar(url),
            count_exc(url),
            count_ast(url),
            count_comma(url),
            no_of_embed(url),
            abnormal_url(url),
            httpSecure(url),
            digit_count(url),
            letter_count(url),
            shortening_service(url),
            have_IP(url),
        ]
    )
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
