from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('app.html')

@app.route('/user')
def user():
    return render_template('user_name.html')

@app.route('/form', methods=['GET','POST'])
def form():
    return render_template('form.html')

@app.route('/RM', methods = ['GET', 'POST'])
def relationship_manager():
    return render_template('relationship_manager.html')

if __name__ == '__main__':
    app.run(debug=True)

    