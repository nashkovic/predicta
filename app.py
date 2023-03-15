from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    team1 = request.form['team1']
    team2 = request.form['team2']
    # Use the existing code to predict the winner
    result = predict_winner(team1, team2)
    return render_template('result.html', result=result, team1=team1, team2=team2)

if __name__ == '__main__':
    app.run(debug=True)
