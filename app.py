from flask import Flask, render_template, request, jsonify
from googletrans import Translator

app = Flask(__name__)

@app.route('/')     
def index():
    return render_template('index.html')
@app.route('/contact')
def Contact():
    return render_template('Contact.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/translate', methods=['POST' , 'GET'])
def translate():
    try:
        input_text = request.form.get('inputText')
        input_language = request.form.get('inputLanguage')
        output_language = request.form.get('outputLanguage')

        # Perform translation using googletrans or your preferred translation library
        translator = Translator()
        translated_text = translator.translate(input_text, src=input_language, dest=output_language).text
        # outputtext = translated_text
        print(translated_text)
       
        return jsonify({'success': True, 'outputtext': translated_text})
       
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})
    

if __name__ == '__main__':
    app.run(debug=True)  