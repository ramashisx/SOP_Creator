from flask import Flask, request, render_template
from bot import edit

app = Flask(__name__)
app.config['SECRET_KEY'] = '89djhff9lhkd93'


@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")


@app.route('/bot', methods=['POST'])
def bot():

    name = request.values["name"]
    college = request.values["college"]
    course = request.values["course"]
    country = request.values["country"]
    family = request.values["family"]
    ielts = request.values["ielts"]
    academics = request.values["academics"]
    experience = request.values["experience"]
    gic = request.values["gic"]
    fees = request.values["fees"]

    final = ""

    f = open("raw/1")
    text = f.read()
    instruction = "Change name to " + name + " and college to " + college + " and course to " \
                  + course + " and country to " + country
    response = edit(text, instruction)
    resp = response.get("choices")[0].get("text").strip()
    print(resp)
    final += resp
    final += "\n"

    f = open("raw/2")
    text = f.read()
    instruction = "Change the subject from psychology to " + course
    response = edit(text, instruction)
    resp = response.get("choices")[0].get("text").strip()
    print(resp)
    final += resp
    final += "\n"

    f = open("raw/3")
    text = f.read()

    instruction = "Change schooling details to " + academics
    response = edit(text, instruction)
    text = response.get("choices")[0].get("text").strip()

    instruction = "Change applying course to " + course
    if len(experience) < 5:
        instruction += " and remove previous experience"
    else:
        instruction += " change previous experience to " + experience
    response = edit(text, instruction)
    resp = response.get("choices")[0].get("text").strip()
    print(resp)
    final += resp
    final += "\n"

    f = open("raw/4")
    text = f.read()
    instruction = "Change ielts score to " + ielts + " and college to " + college + " and applying course to " + course
    response = edit(text, instruction)
    resp = response.get("choices")[0].get("text").strip()
    print(resp)
    final += resp
    final += "\n"

    f = open("raw/5")
    text = f.read()
    instruction = "Change college to " + college + " and applying course to " + course
    response = edit(text, instruction)
    resp = response.get("choices")[0].get("text").strip()
    print(resp)
    final += resp
    final += "\n"

    f = open("raw/6")
    text = f.read()
    instruction = "Change course to " + course
    response = edit(text, instruction)
    resp = response.get("choices")[0].get("text").strip()
    print(resp)
    final += resp
    final += "\n"

    f = open("raw/7")
    text = f.read()
    instruction = "Change family related details with " + family
    response = edit(text, instruction)
    resp = response.get("choices")[0].get("text").strip()
    print(resp)
    final += resp
    final += "\n"

    f = open("raw/8")
    text = f.read()
    instruction = "Change Tution fees to " + fees + " GIC account balance to " + gic
    response = edit(text, instruction)
    resp = response.get("choices")[0].get("text").strip()
    print(resp)
    final += resp
    final += "\n"

    f = open("raw/9")
    text = f.read()
    instruction = "Change ielts score to " + ielts
    response = edit(text, instruction)
    resp = response.get("choices")[0].get("text").strip()
    print(resp)
    final += resp
    final += "\n"

    f = open("raw/10")
    text = f.read()
    instruction = "Change country to " + country + " and college to " + college
    response = edit(text, instruction)
    resp = response.get("choices")[0].get("text").strip()
    print(resp)
    final += resp
    final += "\n"

    f = open("raw/11")
    text = f.read()
    instruction = "Change name to " + name
    response = edit(text, instruction)
    resp = response.get("choices")[0].get("text").strip()
    print(resp)
    final += resp
    final += "\n"

    return final


if __name__ == '__main__':
    app.run(debug=True)
