from flask import Flask, render_template 
app = Flask(__name__)  

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
    }
]

@app.route('/') 
def index():
    return render_template('index.html', jobs=JOBS, company_name='ABC')


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
