from flask import Flask, render_template, request
from grading import process_results
from pdf_generator import generate_pdf
import os

app = Flask(__name__)
UPLOAD_FOLDER = "data"
OUTPUT_FOLDER = "output/reports"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        results = process_results(filepath)

        for student in results["name"].unique():
            student_df = results[results["name"] == student]
            generate_pdf(student, student_df, OUTPUT_FOLDER)

        return "Report cards generated successfully."

    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)
