from flask import Blueprint, render_template
import json

main = Blueprint('main', __name__)

@main.route('/')
def index():
    with open('data/projects.json') as file:
        projects = json.load(file)
    return render_template('index.html', projects=projects)

@main.route('/project/<int:project_id>')
def project_detail(project_id):
    with open('data/projects.json') as file:
        projects = json.load(file)
    project = next((project for project in projects if project['id'] == project_id), None)
    return render_template('project_detail.html', project=project)
