# Smart Academic Advisor for Study Planning and Placement Preparation

## Overview
Smart Academic Advisor is a Flask-based web application that analyzes a student's academic information and provides personalized study planning and placement preparation recommendations.

## Features
- Personalized study hour recommendation based on GPA
- Academic advice based on performance
- Placement preparation suggestions using CGPA
- Aptitude and technical topic recommendations
- Performance comparison graph
- Simple web interface built with Flask

## Technologies Used
- Python
- Flask
- Pandas
- Matplotlib
- HTML
- Excel Datasets (.xlsx)

## Project Structure
```
project/
│── app.py
│── academic_study_dataset.xlsx
│── placement_training_dataset.xlsx
│── templates/
│   ├── index.html
│   └── result.html
│── static/
│   └── graph.png
```

## How It Works
1. User enters Name, Department, Attendance, CGPA, GPA, and Internal Marks.
2. The application reads the academic and placement datasets.
3. It finds the closest GPA and CGPA records.
4. It recommends:
   - Study hours
   - Academic advice
   - Aptitude topics
   - Technical topics
5. A performance comparison graph is generated and displayed.

## Installation
1. Clone the repository.
2. Install dependencies:
```bash
pip install flask pandas matplotlib openpyxl
```
3. Place the Excel datasets in the project folder.
4. Run:
```bash
python app.py
```
5. Open `http://127.0.0.1:5000` in your browser.

## Future Enhancements
- Machine learning based predictions
- Student login system
- Database integration
- Performance history tracking
- Email or notification support

## Author
**Sowmiya J**
