# university-scraper
University Data Scraper is a web-based application that fetches and displays university rankings for selected courses using the QS Top Universities API. Users can filter results based on specific university programs or courses.

- Features

  Fetches rankings for five selected courses:
  
  Computer Science & Information Systems
  Data Science & Artificial Intelligence
  Chemical Engineering
  Civil & Structural Engineering
  Electrical & Electronic Engineering

Uses API-based scraping for real-time data retrieval.
Displays filtered rankings based on course selection.
Presents data on a user-friendly HTML page.

- Installation

  Clone the repository:
  git clone https://github.com/your-username/university-scraper.git
  cd university-scraper
  
  Create a virtual environment (optional but recommended):
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  
  Install dependencies:
  pip install -r requirements.txt

- Usage

  Run the application using:
  python app.py
  Then, open a web browser and visit:
  http://127.0.0.1:5000
  Follow the on-screen prompts to select a course and view rankings.

- File Structure

university-scraper/
│── app.py          # Main application entry point (Flask server)
│── config.py       # Configuration settings
│── main.py         # Handles core logic and user interactions
│── scraper.py      # Scraper for fetching rankings
│── static/         # Contains images related to courses
│── templates/      # HTML templates for the web interface
│── requirements.txt # Dependencies list

- Dependencies

  Python 3.x
  Flask (for web interface)
  Requests (for API calls)

- Contributing
Feel free to fork the repository and submit pull requests for improvements or additional features.

Developed by Aparna Sunil and Anjali Thomas
