from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'clave_secreta_edufutura'

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/quienes_somos')
def quienes_somos():
    return render_template('quienes_somos.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']
        
        # Aquí podrías procesar los datos, guardarlos en una base de datos, etc.
        # Por ahora, solo mostraremos un mensaje de éxito
        flash('¡Mensaje enviado con éxito! Gracias por contactarnos.')
        return redirect(url_for('contacto'))
    
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)
