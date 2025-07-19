from flask import Flask, request, Response
from flask_cors import CORS
from agent_logic import generate_tasks_stream

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Enable CORS for frontend communication

@app.route('/generate-tasks-stream', methods=['POST'])
def stream_tasks():
    goal = request.json.get('goal')
    if not goal:
        return "Missing goal", 400

    def generate():
        for chunk in generate_tasks_stream(goal):
            yield chunk

    return Response(generate(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5000, debug=True)