from flask import Flask, render_template, request
from summary import summarize_text  # Import the text summarization function from summary.py

# Initialize the Flask app
app = Flask(__name__)

# Define the main route for both GET and POST methods
@app.route('/', methods=['GET', 'POST'])
def summarize():
    summary = None           # To store the generated summary
    original_text = None     # To store the input text from the user
    error = None             # To store any error messages

    # Check if the form is submitted via POST
    if request.method == 'POST':
        original_text = request.form.get('text')  # Get the text input from the form

        # If the input is empty or contains only spaces
        if not original_text.strip():
            error = "⚠ Please enter some text to summarize."
        else:
            try:
                # Call the summarization function and store the result
                summary = summarize_text(original_text)
            except Exception as e:
                # Handle any errors during summarization
                error = f"An error occurred during summarization: {str(e)}"

    # Render the HTML template and pass the necessary variables
    return render_template('index.html', summary=summary, original_text=original_text, error=error)

# Run the app if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)