from flask import Flask, request, render_template, redirect, jsonify, flash, session
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


@app.route('/satisfaction_survey/questions/<int:num>', methods=['GET', 'POST'])
def satisfaction_questions(num):
    if 'satisfaction_survey' not in session:
        session['satisfaction_survey'] = []

    if 'satisfaction_question' not in session:
        session['satisfaction_question'] = 0
        
    if num < 0:
        flash("Invalid page")
        return redirect("/satisfaction_survey")
    
    if num > session['satisfaction_question']:
        flash("Please answer the current question first.")
        return redirect(session['satisfaction_question'])
    
    if len(session['satisfaction_survey']) == len(surveys["satisfaction"].questions):
        flash("You already took this")
        return redirect('/')
    
    if request.method == 'POST':
        choice = request.form['choice']
        # Append the answer to the session list
        session['satisfaction_survey'].append(choice)
        
        session.modified = True
        
        # satisfaction_ans.append(choice)
        if (num < len(surveys["satisfaction"].questions) - 1):
            # Update the current question in the session
            session['satisfaction_question'] = num + 1
            
            return redirect(session['satisfaction_question'])
        else:
            return redirect('/thank_you')
    q = surveys["satisfaction"].questions[num]
    question_set = Question(q.question, q.choices, q.allow_text)
    return render_template("question.html", question_set = question_set, num_id = num, type="satisfaction_survey")
        
    

@app.route('/personality_quiz/questions/<int:num>', methods=['GET', 'POST'])
def personality_questions(num):
    if 'personality_quiz' not in session:
        session['personality_quiz'] = []
        
    if 'personality_question' not in session:
        session['personality_question'] = 0
        
    if num < 0:
        flash("Invalid page")
        return redirect("/personality_question")
    
    if num > session['personality_question']:
        flash("Please answer the personality question first.")
        return redirect(session['personality_question'])
        
    if len(session['personality_quiz']) == len(surveys["personality"].questions):
        flash("You already took this")
        return redirect('/')
    
    q = surveys["personality"].questions[num]
    question_set = Question(q.question, q.choices, q.allow_text)
    if request.method == 'POST':
        choice = request.form['choice']
        
        
        if question_set.allow_text:
            input_text = request.form['input_text']
            # satisfaction_ans.append([choice, input_text])
            session['personality_quiz'].append([choice, input_text])
        
        else:
            # satisfaction_ans.append(choice)
            session['personality_quiz'].append([choice])
            
        if (num < len(surveys["satisfaction"].questions) - 1):
            session.modified = True
            session['personality_question'] = num + 1
            return redirect(session['personality_question'])
        else:
            return redirect('/thank_you')
        
    return render_template("question.html", question_set = question_set, num_id = num, type="personality_quiz")

@app.route('/thank_you')
def thank_you():
    # print(satisfaction_ans)
    return render_template('/thank_you.html')

if __name__ == "__main__":
   app.run(debug=True)