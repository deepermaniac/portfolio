from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')

# @app.route("/<username>/<int:post_id>")
# def about(username=None, post_id=None):
#     return render_template('about.html', name=username, id=post_id)

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['Email']
        subject = data['Subject']
        message = data['Message']
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['Email']
        subject = data['Subject']
        message = data['Message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL )
        csv_writer.writerow([email, subject, message])

@app.route('/submitted', methods=['POST', 'GET'])
def submitted():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thanks')
        except:
            return 'did not save to database'
    else:
        return 'Something went Wrong!'
