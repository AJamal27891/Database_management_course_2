from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import plotly.express as px
import pandas as pd
import configparser

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')

db_config = {
    'host': config['mysql']['host'],
    'user': config['mysql']['user'],
    'passwd': config['mysql']['password'],
    'database': config['mysql']['database']
}

@app.route('/')
def index():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT name, email FROM students")
    data = cursor.fetchall()
    
    if not data:
        print("No data found in 'students' table.")
        return render_template('index.html', graph_html="No data available for visualization.")

    df = pd.DataFrame(data)
    print(df.head())  # Debug: print the DataFrame to check its structure

    fig = px.bar(df, x='name', y='score') 

    graph_html = fig.to_html(full_html=False)

    cursor.close()
    conn.close()

    return render_template('index.html', graph_html=graph_html)

# Courses page
@app.route('/courses')
def courses():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM courses")
    course_data = cursor.fetchall()
    
    cursor.close()
    conn.close()

    return render_template('courses.html', courses=course_data)

if __name__ == '__main__':
    app.run(debug=True)
