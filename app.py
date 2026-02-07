from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the saved model
model = joblib.load('linear_regression_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    # Default values (shown as None before any prediction)
    prediction = None
    message = ""
    attendance = None
    test1 = None
    test2 = None
    assignment = None
    study_hours = None

    if request.method == 'POST':
        try:
            # Get user inputs from the form
            attendance = float(request.form['attendance'])
            test1 = float(request.form['test1'])
            test2 = float(request.form['test2'])
            assignment = float(request.form['assignment'])
            study_hours = float(request.form['study_hours'])

            # Create a DataFrame for the model (same structure as training)
            input_data = pd.DataFrame({
                'Attendance (%)': [attendance],
                'Internal Test 1 (out of 40)': [test1],
                'Internal Test 2 (out of 40)': [test2],
                'Assignment Score (out of 10)': [assignment],
                'Daily Study Hours': [study_hours]
            })

            # Predict and round to 1 decimal place
            pred = model.predict(input_data)[0]
            prediction = round(pred, 1)

            # Simple message based on prediction
            if prediction >= 75:
                message = "Excellent!"
            elif prediction >= 60:
                message = "Good!"
            else:
                message = "Needs Improvement"

        except (ValueError, KeyError, TypeError) as e:
            # If any input is missing or not a number
            message = "Please enter valid numbers in all fields."
            prediction = None
            # The input values will still be passed (might be None or partial)

    # Always render the template and pass all variables
    return render_template(
        'index.html',
        prediction=prediction,
        message=message,
        attendance=attendance,
        test1=test1,
        test2=test2,
        assignment=assignment,
        study_hours=study_hours
    )

if __name__ == '__main__':
    app.run(debug=True)
    # If you want to allow access from other devices on the same network:
    # app.run(debug=True, host='0.0.0.0')