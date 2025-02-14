from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/skill_building')
def skill_building():
    return render_template('skill_building.html')

@app.route('/abuse_reporting')
def abuse_reporting():
    return render_template('abuse_reporting.html')

@app.route('/mentorship')
def mentorship():
    return render_template('mentorship.html')

@app.route('/legal_rights')
def legal_rights():
    return render_template('legal_rights.html')

@app.route('/wage_gap')
def wage_gap():
    return render_template('wage_gap.html')

@app.route('/leadership')
def leadership():
    return render_template('leadership.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/wellness')
def wellness():
    return render_template('wellness.html')

@app.route('/businesses')
def businesses():
    return render_template('businesses.html')

if __name__ == '__main__':
    app.run(debug=True)
