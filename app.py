from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import plotly.express as px
import pandas as pd
import configparser
import plotly.graph_objects as go


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

    fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df.Rank, df.State, df.Postal, df.Population],
               fill_color='lavender',
               align='left'))
            ])


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

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO students (name, email) VALUES (%s, %s)", 
                       (name, email))
        conn.commit()

        cursor.close()
        conn.close()

        return redirect(url_for('index'))  # Or to another appropriate page

    return render_template('add_student.html')


if __name__ == '__main__':
    app.run(debug=True)
