from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Load datasets
study_data = pd.read_excel("academic_study_dataset.xlsx")
placement_data = pd.read_excel("placement_training_dataset.xlsx")

# Create static folder if not exists
if not os.path.exists("static"):
    os.makedirs("static")


def get_study_hours(gpa):
    row = study_data.iloc[(study_data['GPA'] - gpa).abs().argsort()[:1]]
    hours = row["Recommended_Study_Hours_Per_Day"].values[0]
    advice = row["Advice"].values[0]
    return hours, advice


def get_placement_topics(cgpa):
    row = placement_data.iloc[(placement_data['CGPA'] - cgpa).abs().argsort()[:1]]
    aptitude = row["Aptitude_Topics"].values[0]
    technical = row["Technical_Topics"].values[0]
    message = row["Message_or_Suggestion"].values[0]
    return aptitude, technical, message


# 📊 GRAPH FUNCTION
def generate_graph(attendance, cgpa, gpa, internal):

    labels = ['Attendance', 'CGPA', 'GPA', 'Internal']

    # Actual values
    actual = [attendance, cgpa * 10, gpa * 10, internal]

    # Ideal values (you can adjust these)
    ideal = [85, 90, 90, 85]

    x = range(len(labels))

    plt.figure()

    plt.plot(x, actual, marker='o', label='Your Performance')
    plt.plot(x, ideal, marker='o', linestyle='--', label='Ideal Performance')

    plt.xticks(x, labels)
    plt.title("Performance Comparison")
    plt.legend()

    plt.savefig("static/graph.png")
    plt.close()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    # NEW INPUTS
    name = request.form['name']
    dept = request.form['department']

    attendance = float(request.form['attendance'])
    cgpa = float(request.form['cgpa'])
    gpa = float(request.form['gpa'])
    internal = float(request.form['internal'])

    hours, advice = get_study_hours(gpa)
    aptitude, technical, message = get_placement_topics(cgpa)

    # Generate graph
    generate_graph(attendance, cgpa, gpa, internal)

    return render_template("result.html",
                           name=name,
                           dept=dept,
                           hours=hours,
                           advice=advice,
                           aptitude=aptitude,
                           technical=technical,
                           message=message,
                           attendance=attendance,
                           cgpa=cgpa,
                           gpa=gpa,
                           internal=internal)


if __name__ == '__main__':
    app.run(debug=True)