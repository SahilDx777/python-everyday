import requests
from requests import Response


def get_res(url) -> Response:
    return requests.get(url)


def show_res_info(response) -> None:
    print("Status:", response.status_code)
    print("OK:", response.ok)
    print("Links:", response.links)
    print("Encoding:", response.encoding)
    print("Is Redirect:", response.is_redirect)
    print("Is Permanent Redirect:", response.is_permanent_redirect)


def main() -> None:
    website = "https://www.google.com"
    response = get_res(website)
    show_res_info(response)


if __name__ == "__main__":
    main()
