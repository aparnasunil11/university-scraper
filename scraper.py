# scraper.py
import requests

def fetch_rankings(api_url):
    """ Fetches rankings from QS API and returns a list of universities. """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://www.topuniversities.com/"
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code != 200:
        print("❌ Failed to fetch rankings.")
        return []

    data = response.json()  # Parse JSON response
    universities = []

    for item in data.get("score_nodes", []):
        rank = item.get("rank_display", "N/A").lstrip("=")
        name = item.get("title", "Unknown University")
        country = item.get("country", "Unknown Country")

        universities.append({"Rank": rank, "University": name, "Country": country})

    return universities
