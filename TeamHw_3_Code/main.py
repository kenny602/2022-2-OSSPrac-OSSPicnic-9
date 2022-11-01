from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')  # default URL
def student():
   return render_template('input_info.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = dict()
      result['Name'] = request.form.get('Name')

      # 학번
      # 성별
      # 학과
      # 프로그래밍 언어
      
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run()
