from flask import Flask, request, render_template, redirect, jsonify,flash
from surveys import *

app = Flask(__name__)
app.secret_key = 'your_secret_key' 

# home
@app.route('/')
def index():
   return render_template("index.html")
@app.route('/satisfaction_survey')
def satisfaction_survey():
    return render_template("satisfaction_survey.html", survey = surveys["satisfaction"])
@app.route('/personality_quiz')
def personality_quiz():
    return render_template("personality_quiz.html", survey = surveys["personality"])

satisfaction_ans = []
personality_ans = []

@app.route('/satisfaction_survey/questions/<int:num>', methods=['GET', 'POST'])
def satisfaction_questions(num):
    if num < 0 or num > len(surveys["satisfaction"].questions) - 1:
        flash("Invalid page")
        return redirect("/satisfaction_survey")
    if request.method == 'POST':
        choice = request.form['choice']
        satisfaction_ans.append(choice)
        if (num < len(surveys["satisfaction"].questions) - 1):
            next_num = num + 1
            return redirect(next_num)
        else:
            return redirect('/thank_you')
    q = surveys["satisfaction"].questions[num]
    question_set = Question(q.question, q.choices, q.allow_text)
    return render_template("question.html", question_set = question_set, num_id = num, type="satisfaction_survey")
        
    

@app.route('/personality_quiz/questions/<int:num>', methods=['GET', 'POST'])
def personality_questions(num):
    q = surveys["personality"].questions[num]
    question_set = Question(q.question, q.choices, q.allow_text)
    if request.method == 'POST':
        choice = request.form['choice']
        
        if question_set.allow_text:
            input_text = request.form['input_text']
            satisfaction_ans.append([choice, input_text])
        else:
            satisfaction_ans.append(choice)
            
        if (num < len(surveys["satisfaction"].questions) - 1):
            next_num = num + 1
            return redirect(next_num)
        else:
            return redirect('/thank_you')
        
    return render_template("question.html", question_set = question_set, num_id = num, type="personality_quiz")

@app.route('/thank_you')
def thank_you():
    print(satisfaction_ans)
    return render_template('/thank_you.html')

if __name__ == "__main__":
   app.run(debug=True)