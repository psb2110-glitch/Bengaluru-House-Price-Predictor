import pickle
import pandas as pd
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

data = pd.read_csv("Corrected_data.csv")
pipe = pickle.load(open("RidgeModel.pkl", "rb"))


def format_indian_currency(num):
    num = f"{num:.2f}"
    integer, decimal = num.split(".")

    if len(integer) > 3:
        last3 = integer[-3:]
        rest = integer[:-3]
        result = ""

        while len(rest) > 2:
            result = "," + rest[-2:] + result
            rest = rest[:-2]

        integer = rest + result + "," + last3

    return integer + "." + decimal


def predict_price(location, sqft, bath, bhk):
    input_df = pd.DataFrame(
        [[location, sqft, bath, bhk]],
        columns=["location", "total_sqft", "bath", "bhk"]
    )
    return pipe.predict(input_df)[0] * 100000


def recommend_locations(budget):
    location_avg = data.groupby("location")["price"].mean() * 100000
    nearby = location_avg[
        (location_avg >= budget * 0.80) & (location_avg <= budget * 1.20)
    ].sort_values().head(6)

    return [
        {"location": location, "avg_price": format_indian_currency(price)}
        for location, price in nearby.items()
    ]


@app.route("/")
def index():
    locations = sorted(data["location"].unique())
    return render_template("index.html", locations=locations)


@app.route("/predict", methods=["POST"])
def predict():
    location = request.form.get("location")
    bhk = float(request.form.get("bhk"))
    bath = float(request.form.get("bath"))
    sqft = float(request.form.get("total_sqft"))

    prediction = predict_price(location, sqft, bath, bhk)

    avg_location_price = data[data["location"] == location]["price"].mean() * 100000

    return jsonify({
        "price": format_indian_currency(prediction),
        "lower_range": format_indian_currency(prediction * 0.90),
        "upper_range": format_indian_currency(prediction * 1.10),
        "avg_location_price": format_indian_currency(avg_location_price),
        "location": location,
        "bhk": int(bhk),
        "bath": int(bath),
        "sqft": int(sqft)
    })


@app.route("/recommend", methods=["POST"])
def recommend():
    budget = float(request.form.get("budget"))
    recommendations = recommend_locations(budget)

    return jsonify({
        "budget": format_indian_currency(budget),
        "recommendations": recommendations
    })


@app.route("/compare", methods=["POST"])
def compare():
    location1 = request.form.get("location1")
    bhk1 = float(request.form.get("bhk1"))
    bath1 = float(request.form.get("bath1"))
    sqft1 = float(request.form.get("sqft1"))

    location2 = request.form.get("location2")
    bhk2 = float(request.form.get("bhk2"))
    bath2 = float(request.form.get("bath2"))
    sqft2 = float(request.form.get("sqft2"))

    price1 = predict_price(location1, sqft1, bath1, bhk1)
    price2 = predict_price(location2, sqft2, bath2, bhk2)

    difference = abs(price1 - price2)

    if price1 > price2:
        better = "Property 2 is cheaper"
    elif price2 > price1:
        better = "Property 1 is cheaper"
    else:
        better = "Both properties have the same predicted price"

    return jsonify({
        "price1": format_indian_currency(price1),
        "price2": format_indian_currency(price2),
        "difference": format_indian_currency(difference),
        "better": better,
        "location1": location1,
        "location2": location2
    })


@app.route("/emi", methods=["POST"])
def emi():
    property_price = float(request.form.get("property_price"))
    down_payment = float(request.form.get("down_payment"))
    interest_rate = float(request.form.get("interest_rate"))
    loan_years = float(request.form.get("loan_years"))

    loan_amount = property_price - down_payment
    monthly_rate = interest_rate / (12 * 100)
    months = loan_years * 12

    emi_amount = loan_amount * monthly_rate * ((1 + monthly_rate) ** months) / (((1 + monthly_rate) ** months) - 1)

    return jsonify({
        "property_price": format_indian_currency(property_price),
        "down_payment": format_indian_currency(down_payment),
        "loan_amount": format_indian_currency(loan_amount),
        "emi": format_indian_currency(emi_amount)
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)