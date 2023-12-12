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

# Home page with visualization
@app.route('/')
def index():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor(dictionary=True)
    
    # Example query to fetch data for visualization
    cursor.execute("SELECT * FROM some_table")
    data = cursor.fetchall()
    
    # Convert data to DataFrame for Plotly
    df = pd.DataFrame(data)
    fig = px.bar(df, x='column1', y='column2') # Modify according to your data

    graph_html = fig.to_html(full_html=False)

    cursor.close()
    conn.close()

    return render_template('index.html', graph_html=graph_html)

# Forum page
@app.route('/forum')
def forum():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    
    cursor.close()
    conn.close()

    return render_template('forum.html', posts=posts)

# Add a new post
@app.route('/add_post', methods=['POST'])
def add_post():
    title = request.form['title']
    content = request.form['content']
    # Add author_id, timestamp, etc. as needed

    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO posts (title, content) VALUES (%s, %s)", (title, content))
    conn.commit()

    cursor.close()
    conn.close()

    return redirect(url_for('forum'))

if __name__ == '__main__':
    app.run(debug=True)
