from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        # Handle form submission and booking logic
        # Example: booking_data = request.form['booking_data']
        return render_template('booking.html')
    return render_template('booking.html')

if __name__ == '__main__':
    app.run(debug=True)
