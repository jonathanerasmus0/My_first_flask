from flask import Flask,render_template,url_for
app = Flask(__name__)


posts = [
    {
        'author': 'JONATHAN ERASMUS DAVIES',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 19, 2024'
    },
    {
        'author': 'JANET DAVIES',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'February, 2024'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('About.html',title='About')

if __name__ == '__main__':
    app.run(debug=True)
    