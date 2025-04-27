from flask import Flask, render_template, request

def convert_euros_to_dollars(amount_euros, exchange_rate=1.1):
    """
    Convierte una cantidad de dinero en euros a dólares.
    :param amount_euros: Cantidad en euros
    :param exchange_rate: Tipo de cambio (por defecto 1.1)
    :return: Cantidad en dólares
    """
    return round(amount_euros * exchange_rate, 2)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    dollars = None
    if request.method == 'POST':
        euros = float(request.form['euros'])
        dollars = convert_euros_to_dollars(euros)
    return render_template('index.html', dollars=dollars)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

