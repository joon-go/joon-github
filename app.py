from flask import Flask
from utils.helper import greet

app = Flask(__name__)

@app.route("/")
def hello():
    return greet("GitLab User")

if __name__ == "__main__":
    app.run(debug=True)

def meters_to_feet(meters: float) -> float:
    """Convert meters to feet."""
    return meters * 3.280839895


# Example usage:
if __name__ == "__main__":
    m = 1.75
    print(f"{m} meters = {meters_to_feet(m):.4f} feet")

def yards_to_meters(yards: float) -> float:
    """Convert yards to meters."""
    return yards * 0.9144

# Example usage:
if __name__ == "__main__":
    y = 5
    print(f"{y} yards = {yards_to_meters(y):.4f} meters")


///commented
