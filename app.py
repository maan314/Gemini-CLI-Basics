from flask import Flask, render_template
import feedparser

app = Flask(__name__)

# RSS feed URL from Cricinfo
RSS_URL = "https://static.cricinfo.com/rss/livescores.xml"

@app.route("/")
def index():
    """
    Fetches and displays live cricket scores from an RSS feed.
    """
    try:
        # Parse the RSS feed
        feed = feedparser.parse(RSS_URL)
        
        # Extract score entries
        scores = [entry.title for entry in feed.entries]

        # Render the template with the scores
        return render_template("index.html", scores=scores, error=None)
    except Exception as e:
        # Handle potential errors (e.g., network issues, parsing errors)
        error_message = f"Error fetching scores: {e}"
        return render_template("index.html", scores=[], error=error_message)

if __name__ == "__main__":
    app.run(debug=True)
