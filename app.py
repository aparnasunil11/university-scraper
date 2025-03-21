from flask import Flask, render_template, request
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np
from config import COURSE_APIS
from scraper import fetch_rankings

app = Flask(__name__)

# Ensure 'static' folder exists for saving graphs
if not os.path.exists("static"):
    os.makedirs("static")

@app.route("/", methods=["GET", "POST"])
def index():
    rankings = []
    selected_course = None
    graph_path = None

    if request.method == "POST":
        choice = request.form["course"]
        
        if choice in COURSE_APIS:
            selected_course, api_url = COURSE_APIS[choice]
            rankings = fetch_rankings(api_url)

            if rankings:
                graph_path = generate_graph(rankings, selected_course)

    return render_template("index.html", courses=COURSE_APIS, rankings=rankings, selected_course=selected_course, graph_path=graph_path)

def generate_graph(rankings, course_name):
    """ Generates a bar chart for university rankings with a brown/beige color scheme """
    # Use only top 10 universities
    df = pd.DataFrame(rankings[:10])
    
    # Set the aesthetic style
    plt.style.use('seaborn-v0_8-whitegrid')
    
    # Create figure with the right size
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Define brown/beige color palette
    brown_beige_palette = [
        "#8B7355",  # Brown
        "#9C8A6A",  # Medium Brown
        "#AD9F80",  # Light Brown
        "#BEB496",  # Tan
        "#CFC9AC",  # Light Tan
        "#E0DEC2",  # Beige
        "#F1F2D8",  # Light Beige
        "#F5F5DC",  # Cream
        "#FFFFF0",  # Ivory
        "#FAEBD7",  # Antique White
    ]
    
    # Reverse the rankings for better visualization (top university at the top)
    universities = [uni["University"].split(" (")[0] for uni in rankings[:10]]
    universities.reverse()
    ranks = list(range(10, 0, -1))
    
    # Create horizontal bar chart
    bars = ax.barh(range(len(universities)), ranks, color=brown_beige_palette)
    
    # Set background color
    fig.patch.set_facecolor('#FFF8E1')  # Cream background
    ax.set_facecolor('#FFF8E1')  # Cream background
    
    # Add university names as y-tick labels
    ax.set_yticks(range(len(universities)))
    ax.set_yticklabels(universities)
    
    # Set x-axis limits and labels
    ax.set_xlim(0, 11)
    ax.set_xlabel('Rank', fontsize=12, color='#5D4037')
    
    # Remove y-axis label
    ax.set_ylabel('')
    
    # Add title with custom styling
    ax.set_title(f'Top 10 Universities for {course_name}', 
                fontsize=16, 
                color='#5D4037', 
                fontweight='bold',
                pad=20)
    
    # Add rank numbers inside or at the end of each bar
    for i, bar in enumerate(bars):
        rank = 10 - i  # Reverse the rank for display
        ax.text(bar.get_width() - 0.5, 
                bar.get_y() + bar.get_height()/2, 
                f"{rank}", 
                ha='center', 
                va='center',
                color='white',
                fontweight='bold',
                fontsize=11)
    
    # Customize grid
    ax.grid(axis='x', linestyle='--', alpha=0.7, color='#D7CCC8')
    
    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#D7CCC8')
    ax.spines['bottom'].set_color('#D7CCC8')
    
    # Customize tick parameters
    ax.tick_params(axis='both', colors='#5D4037')
    
    # Adjust layout and save
    plt.tight_layout()
    graph_path = f"static/{course_name.replace(' ', '_')}.png"
    plt.savefig(graph_path, dpi=100, bbox_inches='tight', facecolor='#FFF8E1')
    plt.close()
    
    return graph_path

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

