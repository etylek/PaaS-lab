from flask import Flask, jsonify, request

app = Flask(__name__)

todos = []

# 1. Health check эндпоинт
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200

# 2. Получение списка задач
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

# 3. Создание новой задачи
@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"error": "Title is required"}), 400
    
    new_todo = {
        "id": len(todos) + 1,
        "title": data["title"],
        "completed": False
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
