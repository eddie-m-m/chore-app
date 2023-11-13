# Create your flask import
from flask import Flask, render_template, session, url_for, redirect, request
import secrets


class ChoreListApp:
    def __init__(self) -> None:
        self.app = Flask(__name__)
        secret_key = secrets.token_hex(32)
        self.app.secret_key = secret_key
        self.register_routes()

    def register_routes(self):
        self.app.add_url_rule('/add_chore', 'add_chore',
                              self.add_chore, methods=['POST'])  # CREATE
        self.app.add_url_rule('/', 'home', self.home)  # READ
        self.app.add_url_rule('/update_chore/<int:chore_id>',
                              'update_chore', self.update_chore, methods=['POST'])  # UPDATE
        self.app.add_url_rule('/delete/<int:chore_id>',
                              'delete_chore', self.delete_chore)  # DELETE

        self.app.add_url_rule('/edit_chore_template/<int:chore_id>',
                              'edit_chore_template', self.edit_chore_template, methods=['GET'])  # Go to edit a chore page
        self.app.add_url_rule('/add_chore_template',
                              'add_chore_template', self.add_chore_template)  # Go to add a chore page

    def home(self):
        chores = Chore.query.all()
        return render_template('home.html', chores=chores)

    def edit_chore_template(self, chore_id):
        chore = Chore.query.get(chore_id)
        return render_template('edit_chore_template.html', chore=chore)

    def add_chore_template(self):
        return render_template('add_chore_template.html')

    # CREATE functionality
    def add_chore(self):
        name = request.form.get('name')
        details = request.form.get('details')
        assigned_child = request.form.get('assigned_child')

        chore = Chore(name, details, assigned_child)
        db.session.add(chore)
        db.session.commit()

        return redirect(url_for('home'))

    # UPDATE functionality
    def update_chore(self, chore_id):
        name = request.form.get('name')
        details = request.form.get('details')
        assigned_child = request.form.get('assigned_child')

        chore = Chore.query.get(chore_id)

        chore.name = name
        chore.details = details
        chore.assigned_child = assigned_child
        db.session.commit()

        return redirect(url_for('home'))

    # DELETE functionality
    def delete_chore(self, chore_id):
        chore = Chore.query.get(chore_id)
        db.session.delete(chore)
        db.session.commit()

        return redirect(url_for('home'))


if __name__ == "__main__":
    with ChoreListApp().app.app_context():
        db.create_all()
    ChoreListApp().app.run(debug=True)
