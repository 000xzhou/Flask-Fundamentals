from flask import Flask, request, render_template, redirect, jsonify
from stories import *

app = Flask(__name__)

# home
@app.route('/')
def index():
   return render_template("index.html", story_templates = story_templates)

# to input story form keys
@app.route('/story_form', methods=["POST"])
def story_form():
   selected_option = request.form['story']
   story_instance = story_templates[selected_option]
   words_list = story_instance.prompts
   print(words_list)
   return render_template(f"story_form.html", selected_story = selected_option, words_list = words_list)

# to display story
@app.route('/story', methods=["POST"])
def storytelling():
   story_value = request.form.get('story_value')
   selected_story = story_templates.get(story_value)
   all_data = {}
   for key in request.form:
        all_data[key] = request.form.get(key)
   finish_story = selected_story.generate(all_data)
   return render_template("story.html", finish_story = finish_story)

# make your own story
@app.route('/make_your_own_story')
def make_your_own():
   return render_template("make_your_own_story.html")

@app.route('/submit_own_story', methods=['POST'])
def submit_story():
    data = request.json
    story_title = data.get('story_title')
    input_keys = data.get('input_keys')
    input_story = " ".join(data.get('input_story'))
    
    new_story = Story(input_keys, input_story)
    story_templates[story_title] = new_story
    return jsonify({"status": "success", "input_keys": input_keys, "input_story": input_story})

if __name__ == "__main__":
   app.run(debug=True)