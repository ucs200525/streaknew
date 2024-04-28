# server.py
from flask import Flask, request, render_template
from datetime import datetime
import os

app = Flask(__name__)

class DuplicateWriteException(Exception):
    pass

def get_streak_count(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1].strip()
                if last_line.isdigit():
                    return int(last_line)
            return 0
    except FileNotFoundError:
        return 0

def create_user_folder(username):
    folder_path = f"users/{username}"  # Folder path relative to the script
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{username}' created successfully.")
    else:
        print(f"Folder '{username}' already exists.")

def save_streak(username, choice, inner_choice, description_choice, description):
    filename = f"users/{username}/streak{choice}.txt"
    today_date = datetime.now().date().isoformat()

    try:
        with open(filename, "r") as file:
            last_write_date = file.readline().strip()
            if last_write_date == today_date:
                raise DuplicateWriteException("You have already written to this file today.")
    except FileNotFoundError:
        pass

    streak_count = get_streak_count(filename) + 1

    try:
        with open(filename, "a") as file:
            file.write(today_date + "\n")
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            file.write(f"Topic: {', '.join(inner_choice)}\n")
            if description_choice == 'yes' and description.strip():
                file.write(f"Description: {description}\n")
                
            file.write(str(streak_count) + "\n")
            return f"You have currently ₹ {streak_count} Rs. Streak saved successfully"
    except FileNotFoundError:
        return "File not found"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_streak', methods=['POST'])
def save_streak_route():
    username = request.form['username']
    password = request.form['password']
    choice = int(request.form['choice'])
    inner_choice = request.form.getlist('inner_choice')
    description_choice = request.form['descriptionChoice']
    description = request.form.get('description', '')

    # Perform user authentication here (validate username and password)
    # For demonstration purposes, let's assume the authentication is successful
    create_user_folder(username)

    # Save streak for the user
    return save_streak(username, choice, inner_choice, description_choice, description)

if __name__ == "__main__":
    app.run(debug=True)
