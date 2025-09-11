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