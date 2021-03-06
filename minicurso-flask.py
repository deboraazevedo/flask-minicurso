from flask import Flask, request, flash, render_template, session
from forms import RegistrationForm
from personagem import Personagem

app = Flask(__name__)

pokemons = []


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate():
        pokemons.append(Personagem(form.nome.data, form.skill.data))
        flash('personagem registrado')
    return render_template('index.html', form=form, pokemons=pokemons)


if __name__ == '__main__':
    app.secret_key = 'why would I tell you my secret key?'
    app.run(port=8080, debug=True)
