from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

# Функция для генерации пароля на основе уровня сложности
def generate_password(complexity):
    if complexity.lower() == 'легкий':
        length = 8
        characters = string.ascii_lowercase
    elif complexity.lower() == 'средний':
        length = 12
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    elif complexity.lower() == 'сложный':
        length = 16
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    elif complexity.lower() == 'очень сложный':
        length = 20
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + '!@#$%^&*()_+-=[]{}|;:,.<>?/`~'
    else:
        return "Неверный уровень сложности. Доступны: Легкий, Средний, Сложный, Очень Сложный."
    
    # Генерация пароля
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = None
    if request.method == 'POST':
        complexity = request.form.get('complexity')
        if complexity:  # Добавил проверку на пустоту
            password = generate_password(complexity)
        else:
            password = "Пожалуйста, выберите уровень сложности."
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)