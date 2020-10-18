from flask import Flask, render_template
app = Flask(__name__, template_folder='G:\\tamu\\3RD SEM\\Hubspot_assess\\templates')
from flask import request, jsonify
import pandas as pd

import os

PEOPLE_FOLDER = os.path.join('static', 'photo')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route('/')
def index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'technology_experience.png')
    major_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'majors.png')
    workshop_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'workshop.png')
    return render_template('index.html', user_image = full_filename, major = major_filename, workshop = workshop_filename)



@app.route('/background_check_throughputrate', methods=['GET', 'POST'])
def background_check_throughputrate():
    if request.method == 'POST':
        text = request.form['throughput_rate_text']
        processed_text = str(text)
        df = pd.read_csv("G:\\tamu\\3RD SEM\\Hubspot_assess\\Team_clusters.csv")
        value = "Congratulations you are matched with team "+ str(int(df.loc[df['userid'] == processed_text ]['Cluster'])+1)

        throughput = value
        return jsonify(throughput)


if __name__ == "__main__":
  app.run(debug=True)
