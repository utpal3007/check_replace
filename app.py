from flask import Flask

app = Flask(__name__)

@app.route('/')
def replace_sentence():
    original_sentence = "We really like the new security features of Google"
    modified_sentence = original_sentence.replace("Google", "Google©")
    return modified_sentence

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
