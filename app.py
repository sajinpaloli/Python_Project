from flask import Flask, render_template, jsonify, request
from database import get_data
import pandas as pd

app = Flask(__name__)
collection= get_data()

def calculate_metrics(filters=None):
    query = {}
    if filters:
        for key, value in filters.items():
            if value:
                query[key] = value

    
    data = list(collection.find(query))

    if not data:
        return {
            "avg_exam_score": 0,
            "avg_study_hours": 0,
            "avg_attendance": 0,
            "gender_distribution": {},
            "school_type_distribution": {},
        }


    total_exam_score = sum(item.get("Exam_Score", 0) for item in data)
    total_study_hours = sum(item.get("Hours_Studied", 0) for item in data)
    total_attendance = sum(item.get("Attendance", 0) for item in data)


    gender_distribution = {item["_id"]: item["count"] for item in collection.aggregate([
        {"$group": {"_id": "$Gender", "count": {"$sum": 1}}}
    ])}

    school_type_distribution = {item["_id"]: item["count"] for item in collection.aggregate([
        {"$group": {"_id": "$School_Type", "count": {"$sum": 1}}}
    ])}

    metrics = {
        "avg_exam_score": round(total_exam_score / len(data), 2),
        "avg_study_hours": round(total_study_hours / len(data), 2),
        "avg_attendance": round(total_attendance / len(data), 2),
        "gender_distribution": gender_distribution,
        "school_type_distribution": school_type_distribution,
    }
    return metrics

@app.route("/")
def index():
    return render_template("dashboard.html")

@app.route("/api/data", methods=["POST"])
def api_data():
    filters = request.json
    metrics = calculate_metrics(filters)
    return jsonify(metrics)

if __name__ == "__main__":
    app.run(debug=True)
