from flask import Flask, request
import csv

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_form():

    name = request.form.get('name')
    age = request.form.get('age')
    gender = request.form.get('gender')
    height = request.form.get('height')
    weight = request.form.get('weight')


    bmi = float(weight) / ((float(height)/100) ** 2)


    with open('bmi_data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, age, gender, height, weight, bmi])

    # 返回响应
    return '表单提交成功！'

app.run()