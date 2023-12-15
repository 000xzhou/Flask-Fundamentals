from flask import Flask, request, render_template, redirect
from stories import *

app = Flask(__name__)


@app.route('/')
def index():
   return render_template("index.html", story_templates = story_templates)

@app.route('/story_form', methods=["POST"])
def story_form():
   selected_option = request.form['story']
   print(selected_option)
   return render_template(f"story_form.html", selected_story = selected_option)

@app.route('/story', methods=["POST"])
def storytelling():
   place = request.form.get("place")
   noun = request.form.get("noun")
   verb = request.form.get("verb")
   adjective = request.form.get("adjective")
   plural_noun = request.form.get("plural_noun")
   story_value = request.form.get('story_value')
   selected_story = story_templates.get(story_value)
   # finish_story = story1.generate({"place": place, "verb": verb, "adjective": adjective, "plural_noun": plural_noun, "noun": noun})
   finish_story = selected_story.generate({
        "place": place, "noun": noun, "verb": verb, 
        "adjective": adjective, "plural_noun": plural_noun
   })
   return render_template("story.html", finish_story = finish_story)

# make your own story
@app.route('/make_your_own_story')
def make_your_own():
   return render_template("make_your_own_story.html")
@app.route('/own_story_lines', methods=["POST"])
def own_story_lines():
   line1 = request.form.get("line-1")
   line2 = request.form.get("line-2")
   line3 = request.form.get("line-3")
   line4 = request.form.get("line-4")
   story_name = request.form.get("story_name")
   
   story_text = f"{line1} {{place}}, {line2} {{adjective}} {{noun}}. {line3} {{verb}} {{plural_noun}}. {line4}."
   # should get keys like "place", etc from form... and then put it in a form... maybe later 
   story_templates[story_name] = Story(
   ["place", "noun", "verb", "adjective", "plural_noun"], story_text)
   return redirect('/')

app.run(debug=True)