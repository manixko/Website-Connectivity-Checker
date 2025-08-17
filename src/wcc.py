import requests
import argparse

def fix_url_format(url):
    if url.startswith('http://'):
        url = url[len('http://'):]
    elif url.startswith('https://'):
        url = url[len('https://'):]
    
    if url.startswith('www.'):
        url = url[len('www.'):]

    formatted_url = 'https://www.' + url
    
    return formatted_url


def wcc(url):
    formatted_url = fix_url_format(url=url)
    try:
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        response = requests.get(url=formatted_url, headers=header, timeout=5)

        if response.status_code == 200:
            return True
        else:
            return False
    except Exception:
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Website Conectivity Checker")
    parser.add_argument('-u', '--url', help="The url of website to check connectivity")

    args = parser.parse_args()

    print("\nchecking...")
    connectivity = wcc(url=args.url)

    if connectivity == True:
        print(f"|>>> {fix_url_format(url=args.url)} is connect!\n")
    elif connectivity == False:
        print(f"|>>> {fix_url_format(url=args.url)} is NOT connect!!!\n")
