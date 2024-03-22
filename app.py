from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample portfolio data
portfolio = [
    {
        'title': 'Face Recognition',
        'description': 'Built with OpenCV',
        # 'image': 'project1.jpg'
    },
    {
        'title': 'Online BookStore',
        'description': 'Built with React with Firebase',
        # 'image': 'project2.jpg'
    },
    {
        'title': 'Bike Price Prediction',
        'description': 'Machine Learning Built on FLask',
        # 'image': 'project3.jpg'
    },
    {
        'title': "College Prediction Website (Currently Working)",
        'description':'Machine Learning Built on Flask'
    }
]

# Route for portfolio page
@app.route('/')
def portfolio_page():
    return render_template('portfolio.html', portfolio=portfolio)

# Route for contact us form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Here you can add code to handle the contact form submission, like sending emails, saving to a database, etc.
        
        return redirect(url_for('thank_you'))
    
    return render_template('contact.html')

# Route for thank you page
@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)
