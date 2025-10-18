from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        test = request.form['userInput']
        test2 = request.form['userInput2']
        return f"You typed: {test}{test2}"
    else:
        return '''
            <form method="post">
                <input name="userInput">
                <input name="userInput2">
                <button type="submit">Submit</button>
            </form>
        '''

if __name__ == '__main__':
    app.run(debug=True)