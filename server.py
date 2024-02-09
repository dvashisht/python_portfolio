from flask import Flask, render_template, url_for, request, redirect
import csv
# Create an instance of flask app and set the name __main__:
app = Flask(__name__)
print(__name__)

# @app.route("/")  # This is a Decorator. It's root/home route.
# def hello_world():
#     return "<p>Hello, Dinesh!</p>"


# This is a Decorator. It's root/home route.
@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', dialect='excel',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # return 'Form submitted!!!!'
    if request.method == 'POST':
        try:
            # request the form data and convert it to a Dictionary:
            data = request.form.to_dict()
            # print(data)
            # write_to_file(data)
            write_to_csv(data)
            # return 'Form submitted.'
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database.'
        else:
            return 'Something went wrong, try again!'

# @app.route("/about.html")
# def about():
#     return render_template('about.html')


# @app.route("/works.html")
# def work():
#     return render_template('works.html')


# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')
