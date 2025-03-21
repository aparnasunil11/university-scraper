# main.py
from config import COURSE_APIS
from scraper import fetch_rankings

def main():
    """ Displays course options and fetches rankings for the selected course. """

    print("\n📚 Available Courses:")
    for key, (course_name, _) in COURSE_APIS.items():
        print(f"{key}. {course_name}")

    choice = input("\nEnter the number of the course you want rankings for: ").strip()

    if choice in COURSE_APIS:
        course_name, api_url = COURSE_APIS[choice]
        print(f"\n🔍 Fetching rankings for {course_name}...\n")

        rankings = fetch_rankings(api_url)

        if rankings:
            for uni in rankings[:10]:  # Show top 10 universities
                print(f"{uni['Rank']}. {uni['University']} ({uni['Country']})")
        else:
            print("❌ No rankings found.")

    else:
        print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
