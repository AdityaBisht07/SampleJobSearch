from flask import Flask, render_template 
app = Flask(__name__)  #here we created an app, an app is simply an object of the class Flask
#

JOBS = [
    {
        'id': 1,
        'title': 'Front-End Engineer',
        'location': 'Gurgaon, India',
        'Salary':'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Analyst',
        'location': 'Hyderabad, India',
        'Salary':'Rs. 13,00,000'
    },{
        'id': 3,
        'title': 'Back-End Engineer',
        'location': 'Bengaluru, India',
        'Salary':'Rs. 15,00,000'
    },
    {
        'id': 4,
        'title': 'Data Scientist',
        'location': 'California, USA',
        'Salary':'$ 11,000'
    },
]

@app.route('/')  #route is a part of the url after the domain name, here also ('/') is the empty route, which is basically just the homepage of your website
def index():
    return render_template('index.html', jobs=JOBS)

@app.route('/about')
def about(): # here we defined a function about, which simply returns "This is the about page"
    return "This is the about page. ADITYA"

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
