from app import create_app, db, cli
from app.models import User, Post, Message, Notification, Task, Tool

app = create_app()
cli.register(app)
with app.app_context():
    db.create_all()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message,
            'Notification': Notification, 'Task': Task, 'Tool': Tool}
