from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import os

api = Flask(__name__)

# MySQL configurations
api.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST", "db")
api.config["MYSQL_USER"] = os.getenv("MYSQL_USER", "user")
api.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD", "password")
api.config["MYSQL_DB"] = os.getenv("MYSQL_DB", "quotesdb")

mysql = MySQL(api)


@api.route("/api/quotes", methods=["GET"])
def get_quotes():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM quotes")
    quotes = cursor.fetchall()
    cursor.close()
    return jsonify([{"id": q[0], "quote": q[1], "author": q[2]} for q in quotes])


@api.route("/health", methods=["GET"])
def health():
    return "OK", 200


@api.route("/api/quotes", methods=["POST"])
def add_quote():
    content = request.json["quote"]
    author = request.json["author"]
    cursor = mysql.connection.cursor()
    cursor.execute(
        "INSERT INTO quotes (quote, author) VALUES (%s, %s)", (content, author)
    )
    mysql.connection.commit()
    quote_id = cursor.lastrowid
    cursor.close()
    return jsonify({"id": quote_id, "quote": content, "author": author}), 201


if __name__ == "__main__":
    # Use the PORT environment variable provided by Beanstalk, defaulting to 5001 for local development
    port = int(os.environ.get("PORT", 5001))
    api.run(host="0.0.0.0", port=port)


# from flask import Flask, jsonify, request
# from flask_mysqldb import MySQL
# import os

# api = Flask(__name__)

# # MySQL configurations
# api.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST", "db")
# api.config["MYSQL_USER"] = os.getenv("MYSQL_USER", "user")
# api.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD", "password")
# api.config["MYSQL_DB"] = os.getenv("MYSQL_DB", "quotesdb")

# mysql = MySQL(api)


# @api.route("/api/quotes", methods=["GET"])
# def get_quotes():
#     cursor = mysql.connection.cursor()
#     cursor.execute("SELECT * FROM quotes")
#     quotes = cursor.fetchall()
#     cursor.close()
#     return jsonify([{"id": q[0], "quote": q[1], "author": q[2]} for q in quotes])


# @api.route("/health")
# def health():
#     return "OK", 200


# @api.route("/api/quotes", methods=["POST"])
# def add_quote():
#     content = request.json["quote"]
#     author = request.json["author"]
#     cursor = mysql.connection.cursor()
#     cursor.execute(
#         "INSERT INTO quotes (quote, author) VALUES (%s, %s)", (content, author)
#     )
#     mysql.connection.commit()
#     quote_id = cursor.lastrowid
#     cursor.close()
#     return jsonify({"id": quote_id, "quote": content, "author": author})


# if __name__ == "__main__":
#     api.run(host="0.0.0.0", port=5001)
#     # api.run(debug=True, host="0.0.0.0", port=5001)
