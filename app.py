import os
from flask import Flask, request, render_template
import joblib
import re

app = Flask(__name__)

# Load your trained model
model_path = os.path.join('model', 'bert.pkl')
model = joblib.load(model_path)


# function to check blanks in sentence
def check_blanks(sentence):

  blank_count = len(re.findall(r"\_+", sentence)) # Use regular expression to match any sequence of underscores
  return blank_count


# function to convert '________' into '[MASK]'
def mask_blank(blanked_sentence):

  start_index = blanked_sentence.index("_")  # Find the index of the first _
  end_index = blanked_sentence.rfind("_")   # Find the index of the last _
  masked_sentence = blanked_sentence[:start_index] + "[MASK]" + blanked_sentence[end_index+1:]
  return masked_sentence


# replace '_______' with word
def fill_the_blank(blanked_sentence, word):

  start_index = blanked_sentence.index("_")  # Find the index of the first _
  end_index = blanked_sentence.rfind("_")   # Find the index of the last _
  filled_sentence = blanked_sentence[:start_index] + "<span class='hightlighted'>" + word + "</span>" + blanked_sentence[end_index+1:]
  return filled_sentence
  


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_sentence = request.form['input_value']
    blank_count = check_blanks(input_sentence)

    if blank_count == 1:
        masked_sent = mask_blank(input_sentence)

        all_predictions = model.predict([[(masked_sent)]]) 
        best_word = all_predictions[0]['token_str']
        final_sentence = fill_the_blank(input_sentence, best_word)
        return render_template('index.html', output=final_sentence)
    else:
       msg = "<span class='col-red'>There should be one blank (_________) in your sentence.</span>"
       return render_template('index.html', output=msg)

if __name__ == "__main__":
    app.run(debug=True)
