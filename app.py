from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Example to handle form submission
    student_name = request.form.get('student_name')
    roll_number = request.form.get('roll_number')
    
    # You can save this data to a database or log it
    print(f"Student Name: {student_name}, Roll Number: {roll_number}")
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
