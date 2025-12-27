from flask import Flask, render_template, request

app = Flask(__name__)

def averageMarks(mark1, mark2, mark3):
    return (mark1 + mark2 + mark3) / 3

def get_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        name = request.form["name"]
        m1 = float(request.form["mark1"])
        m2 = float(request.form["mark2"])
        m3 = float(request.form["mark3"])

        avg = averageMarks(m1, m2, m3)
        grade = get_grade(avg)

        result = {
            "name": name,
            "average": round(avg, 2),
            "grade": grade
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
