from flask import Flask, jsonify, request, render_template
import tictactoe as ttt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['GET'])
def start():
    board = ttt.initial_state()
    return jsonify({'board': board})

@app.route('/move', methods=['POST'])
def move():
    data = request.get_json()
    board = data.get('board')
    row = int(data.get('row'))
    col = int(data.get('col'))
    if board is None or row is None or col is None:
        return jsonify({'error': 'Missing data'}), 400

    try:
        action = (row, col)
        if not ttt.actions(board):
            return jsonify({'error': 'Game over or invalid move'}), 400
        new_board = ttt.result(board, action)
        return jsonify({'board': new_board, 'gameOver': ttt.terminal(new_board)})
    except Exception as e:
        return jsonify({'error': 'An error occurred processing the move', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
