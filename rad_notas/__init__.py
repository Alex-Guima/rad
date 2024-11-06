import os

from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def notas():
        return """
        <h1>Trabalho de Desenvolvimento de Software 2024/2 - Sistema de Notas de Alunos</h1>

        Para visualizar o projeto completamente acesse a rota /alunos
        """

    from . import alunos
    app.register_blueprint(alunos.bp)


    return app
