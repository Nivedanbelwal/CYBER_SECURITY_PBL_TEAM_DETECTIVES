from flask import Flask, request, jsonify
from flask_cors import CORS
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import re
from string import punctuation

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})


nltk.download('punkt')
nltk.download('stopwords') 

def clean_text(text):
    
    text = re.sub(r'\s+', ' ', text)
    
    text = re.sub(r'[^\w\s.,!?-]', '', text)
    return text.strip()

def summarize_text(text, num_sentences=5):
    
    sentences = sent_tokenize(text)
    
   
    stop_words = set(stopwords.words('english'))
    

    word_tokens = word_tokenize(text.lower())
    word_tokens = [word for word in word_tokens if word not in stop_words and word not in punctuation]
    
    
    freq_dist = FreqDist(word_tokens)
    
    
    sentence_scores = {}
    for i, sentence in enumerate(sentences):
        for word in word_tokenize(sentence.lower()):
            if word in freq_dist:
                if i not in sentence_scores:
                    sentence_scores[i] = freq_dist[word]
                else:
                    sentence_scores[i] += freq_dist[word]
    
    
    top_sentence_indices = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)[:num_sentences]
    top_sentence_indices = sorted([i for i, _ in top_sentence_indices])
    
    #
    return [sentences[i] for i in top_sentence_indices]

def extract_key_points(text):
   
    sentences = sent_tokenize(text)
    
    
    important_keywords = [
        'must', 'shall', 'will', 'agree', 'accept', 'prohibited',
        'required', 'responsibility', 'liability', 'rights', 'obligations',
        'termination', 'cancellation', 'refund', 'payment', 'privacy',
        'data', 'information', 'security', 'copyright', 'trademark',
        'warranty', 'guarantee', 'compensation', 'damages', 'indemnify',
        'breach', 'violation', 'enforce', 'govern', 'jurisdiction'
    ]
    
 
    scored_sentences = []
    for i, sentence in enumerate(sentences):
        score = 0
        # Check for important keywords
        for keyword in important_keywords:
            if keyword.lower() in sentence.lower():
                score += 2
        # Give higher weight to sentences at the beginning
        position_weight = 1 - (i / len(sentences))
        score += position_weight
        scored_sentences.append((sentence, score))
    
    # Get top 5 sentences
    top_sentences = sorted(scored_sentences, key=lambda x: x[1], reverse=True)[:5]
    return [s[0] for s in top_sentences]

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        # Clean the text
        cleaned_text = clean_text(text)
        
        # Generate summary
        summary = summarize_text(cleaned_text)
        key_points = extract_key_points(cleaned_text)
        
        return jsonify({
            'summary': ' '.join(summary),
            'key_points': key_points
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) 