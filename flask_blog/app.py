from flask import Flask, render_template, request
import datetime
import database

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    database.create_tables("entries")

    if request.method == "POST":
        entry_content = request.form.get("content")
        database.create_entry("entries", entry_content,
                              datetime.datetime.today().strftime("%b %d - %H:%M"))

    return render_template("home.html", entries=database.retrieve_entries("entries"))


@app.route("/bookmarks", methods=["GET", "POST"])
def bookmarks():
    database.create_tables("bookmarks")

    if request.method == "POST":
        entry_content = request.form.get("content")
        database.create_entry("bookmarks", entry_content,
                              datetime.datetime.today().strftime("%b %d - %H:%M"))

    return render_template("home.html", entries=database.retrieve_entries("bookmarks"))

@app.route("/calendar")
def calendar():
    return render_template("calendar.html")


@app.route("/admin-delete-db")
def delete_databases():
    database.delete()
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
