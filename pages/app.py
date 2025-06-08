import streamlit as st
from transformers import BertTokenizer, TFBertModel, DistilBertTokenizerFast, TFDistilBertModel
import tensorflow as tf
from tensorflow.keras.layers import Input, Conv1D, GlobalMaxPooling1D, Dense, Dropout, Lambda, LSTM, Bidirectional, Attention, LayerNormalization
from tensorflow.keras.metrics import BinaryAccuracy
import warnings
import heapq
warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="SNG - BERT Analyzer",
    page_icon="🌟",
    layout="centered",
    initial_sidebar_state='collapsed'
)

# Importing the pre-trained BERT model and tokenizer
tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')
bert_model = TFDistilBertModel.from_pretrained('distilbert-base-uncased')

if 'comments' not in st.session_state:
    st.session_state['comments'] = []


st.title("🌟 SNG BERT Analyzer")
st.markdown("Write your comment below and let our BERT model analyze it for you!")

def text_conversion(text):
    input_text = tokenizer(
    text,
    truncation = True,
    padding = 'max_length',
    max_length = 128,
    return_tensors = 'tf'
    )

    input_tensor = [input_text['input_ids'], input_text['attention_mask']]
    return input_tensor

def extract_bert_embeddings(inputs):
    outputs = bert_model(inputs)
    return outputs.last_hidden_state  

# Comment input
with st.form(key='comment_form'):
    comment_text = st.text_area("Leave a comment")
    submit_button = st.form_submit_button("Post")

# Prediction
text = ""
text = comment_text if comment_text else text

model = tf.keras.models.load_model("sng-bi-lstm-cnn.h5", custom_objects={'extract_bert_embeddings': extract_bert_embeddings})
input_tensor = text_conversion(text)

prediction = model.predict(input_tensor)
# prediction = prediction[1:]
print("\n\n")
print(text)
print(prediction)

# Displaying the prediction
largest_indices = heapq.nlargest(3, range(len(prediction[0])), key=prediction[0].__getitem__)
print("Indices of the three largest numbers:", largest_indices)


class_names = ['obscene','identity_attack','insult','threat','sexually_explicit']
pred_classes = [class_names[largest_indices[0]],
                class_names[largest_indices[1]],
                class_names[largest_indices[2]]]

# Displaying the results

if submit_button:
    st.subheader('Analysis')
    if comment_text:
        def check():
            if (pred_classes[0] == 'insult'):
                if prediction[0][largest_indices[1]] < 0.4:
                    return True
            else:
                if max(prediction[0]) < 0.4:
                    return True
                else:
                    return False
                
        check = check()
        if check:
            print(check)
            st.markdown(
            f"""
            <div style="display: flex; justify-content: center; align-items: center;">
                <div style="text-align: center;">
                    <span style="background-color:#d0f0c0; padding:10px; border-radius:10px; margin:10px;">
                        <strong style="color:#388e3c;">Non Toxic</strong>
                    </span>
                </div>
            </div>
            """, unsafe_allow_html=True
            )

            print('Non Toxic', '\n\n')
        else:
            print(check)
            st.markdown(
            f"""
            <div style="display: flex; justify-content: center; align-items: center;">
                <div style="text-align: center;">
                    <span style="background-color:#ffcccb; padding:10px; border-radius:10px; margin:10px;">
                        <strong style="color:#d32f2f;">{pred_classes[0]}</strong>
                    </span>
                    <span style="background-color:#d0f0c0; padding:10px; border-radius:10px; margin:10px;">
                        <strong style="color:#388e3c;">{pred_classes[1]}</strong>
                    </span>
                    <span style="background-color:#add8e6; padding:10px; border-radius:10px; margin:10px;">
                        <strong style="color:#1976d2;">{pred_classes[2]}</strong>
                    </span>
                </div>
            </div>
            """, unsafe_allow_html=True
            )
            
            print(pred_classes)
            print("\n\n")
    else:
        st.warning("Please enter a comment to analyze.")

