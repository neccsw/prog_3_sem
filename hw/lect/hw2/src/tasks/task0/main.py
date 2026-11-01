import requests


def main():
    try:
        response = requests.get("https://api.github.com", timeout=5)
        print("Status code:", response.status_code)
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        print("Error: could not complete the GitHub API request:", error)


if __name__ == "__main__":
    main()
