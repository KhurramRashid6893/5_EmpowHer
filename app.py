from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key="AIzaSyDS1336LlHoyxTfvkJCgRRl4cpO34jtfl4")
model = genai.GenerativeModel("gemini-2.0-flash")

# AI Assistant Route for Abuse Reporting
@app.route('/ai_assistant', methods=['POST'])
def ai_assistant():
    data = request.get_json()
    user_input = data.get("prompt", "")

    if not user_input:
        return jsonify({"response": "Please enter a message for the AI assistant."})

    try:
        response = model.generate_content(user_input)
        cleaned_text = response.text.strip().replace("*", "").replace("-", "").replace("\n\n", "\n")
        return jsonify({"response": cleaned_text})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

# Existing AI route for startup idea generator
@app.route('/generate-idea', methods=['POST'])
def generate_idea():
    data = request.get_json()
    user_prompt = data.get("prompt", "")
    prompt = f"Suggest some innovative small-scale or home-based business ideas for women based on the following interests: {user_prompt}. Keep them practical and inspiring."

    try:
        response = model.generate_content(prompt)
        idea_text = response.text.strip()
        return jsonify({"idea": idea_text})
    except Exception as e:
        return jsonify({"idea": "Sorry, I couldn't generate an idea at the moment. Please try again later."})

@app.route('/ai_mentor', methods=['POST'])
def ai_mentor():
    data = request.get_json()
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"response": "No input provided."})

    try:
        response = model.generate_content(prompt)
        raw_text = response.text.strip()

        cleaned_text = raw_text.replace("*", "").replace("-", "").replace("\n\n", "\n").strip()
        lines = cleaned_text.split('\n')
        spaced_lines = [line.strip() + "\n" for line in lines if line.strip()]
        limited_text = '\n\n'.join(spaced_lines[:15])

        return jsonify({"response": limited_text})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

# Page Routes
@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/skill_building')
# def skill_building():
#     return render_template('skill_building.html')


@app.route('/skill_building', methods=['GET', 'POST'])
def skill_building():
    response = None
    if request.method == 'POST':
        interest = request.form.get("interest", "")
        if interest:
            prompt = f"""
You are a course recommendation assistant for women's empowerment. A user is interested in "{interest}".
Suggest 5 to 10 beginner-friendly online courses or platforms that are easy to start and accessible.
Format your response as a numbered list with course title and platform.
Only include relevant, readable suggestions without explanations or URLs.
"""
            try:
                result = model.generate_content(prompt)
                response = result.text
            except Exception as e:
                response = "Sorry, there was an error while fetching suggestions."
    return render_template("skill_building.html", response=response)

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

# if __name__ == '__main__':
#     #app.run(debug=True)
#     app.run(host = "0,0,0,0", port = 5000)
    
if __name__ == '__main__':
    #init_db()
    app.run(host='0.0.0.0', port=5000)
