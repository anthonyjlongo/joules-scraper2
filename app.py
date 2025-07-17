from flask import Flask, render_template, request, send_file
import os
from utils.scraper import run_scraper

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        address = request.form.get("address")
        if address:
            # This will run the scraper and generate a CSV
            csv_path = run_scraper(address)
            return send_file(csv_path, as_attachment=True)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
