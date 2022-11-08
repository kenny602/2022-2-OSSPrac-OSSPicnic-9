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
      # 학번 (이상준)
      result['StudentNumber'] = request.form.get('inputS_num')
      
      # 성별 (김재현)
      result['Gender'] = request.form.get('inputGender')
      # 학과
      result_lst = request.form.getlist('ProLang')
      result['languages'] = ','.join(result_lst) # 프로그래밍 언어 (배서윤)
      
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True, port = 80)
