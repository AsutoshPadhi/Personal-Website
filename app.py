from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/test')
# def test():
#     return render_template('test.html')

# @app.route('/new')
# def new_page():
#     return render_template('new.html')

# @app.route('/resume')
# def resume():
#     return render_template('resume.html')

if __name__ == "__main__":
    app.run(debug=True)