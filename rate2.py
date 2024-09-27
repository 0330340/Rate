from flask import Flask, render_template, request

app = Flask(__name__)

# Startseite mit den Berechnungen
@app.route("/", methods=["GET", "POST"])
def index():
    rate_on_turnover = None
    dso = None
    rate_on_outstandings = None
    if request.method == "POST":
        rate_on_turnover_input = request.form.get("turnover")
        dso_input = request.form.get("dso")
        rate_on_outstandings_input = request.form.get("receivables")

        try:
            # Berechnung der fehlenden Variablen
            if rate_on_turnover_input and dso_input and not rate_on_outstandings_input:
                rate_on_outstandings = float(rate_on_turnover_input) * (30 / float(dso_input))
            elif dso_input and rate_on_outstandings_input and not rate_on_turnover_input:
                rate_on_turnover = float(rate_on_outstandings_input) / 30 * float(dso_input)

            # Formatierung der berechneten Werte
            if rate_on_outstandings is not None:
                rate_on_outstandings = "{:,.5f}%".format(rate_on_outstandings).replace(',', 'X').replace('.', ',').replace('X', '.')
            if rate_on_turnover is not None:
                rate_on_turnover = "{:,.5f}%".format(rate_on_turnover).replace(',', 'X').replace('.', ',').replace('X', '.')

        except ValueError:
            return render_template("index.html", error="Ungültige Eingabe!")

    return render_template("index.html", rate_on_turnover=rate_on_turnover, dso=dso, rate_on_outstandings=rate_on_outstandings)

if __name__ == "__main__":
    app.run(debug=True)
