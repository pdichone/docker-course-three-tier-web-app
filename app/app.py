# from flask import Flask, render_template, request, redirect, url_for
# import requests
# import os

# app = Flask(__name__)

# # Get the API URL from the environment variable or default to localhost for development
# API_URL = os.environ.get("API_URL", "http://localhost:5001")


# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         # Capture the quote and author from the form
#         quote = request.form["quote"]
#         author = request.form["author"]
#         # Post the quote to the API
#         response = requests.post(
#             f"{API_URL}/api/quotes", json={"quote": quote, "author": author}
#         )
#         if response.status_code == 201:
#             # Redirect to the index page if the POST is successful
#             return redirect(url_for("index"))
#         else:
#             # You might want to handle API errors differently
#             return "Error: Unable to save quote", 500
#     else:
#         # GET request to fetch quotes from the API
#         response = requests.get(f"{API_URL}/api/quotes")
#         if response.status_code == 200:
#             quotes = response.json()
#         else:
#             # Handle the case where the API is down or returning an error
#             quotes = []
#             print(
#                 f"Error: Unable to fetch quotes. API responded with status code {response.status_code}"
#             )

#         return render_template("index.html", quotes=quotes)


# # The main entry point for running the Flask app
# if __name__ == "__main__":
#     # Use the PORT environment variable set by Beanstalk, defaulting to 5000 for local development
#     port = int(os.environ.get("PORT", 5002))
#     app.run(host="0.0.0.0", port=port)


# ==== Old code that works only for local dev ====

from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)


# for beanstalk deployment use the url that we created:
## quotes-app-itox.us-west-2.elasticbeanstalk.com
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        quote = request.form["quote"]
        author = request.form["author"]
        requests.post(
            "http://api:5001/api/quotes", json={"quote": quote, "author": author}
        )
        # requests.post(
        #     "http://bonni-test-env.eba-h7hph2uq.us-west-2.elasticbeanstalk.com/api/quotes",
        #     json={"quote": quote, "author": author},
        # )
        return redirect(url_for("index"))
    else:
        quotes = requests.get("http://api:5001/api/quotes").json()
        return render_template("index.html", quotes=quotes)
        # quotes = requests.get(
        #     "http://bonni-test-env.eba-h7hph2uq.us-west-2.elasticbeanstalk.com/api/quotes"
        # ).json()
        # return render_template("index.html", quotes=quotes)


# new
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
    # app.run(debug=True, host="0.0.0.0", port=5002)
