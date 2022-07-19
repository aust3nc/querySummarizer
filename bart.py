#imports
import torch
from transformers import BartTokenizer, BartForConditionalGeneration
import streamlit as st
import os

@st.cache
def buildDirectory():
    os.system('git clone https://github.com/huggingface/transformers')
    os.system('cd transformers')
    os.system('pip install transformers')

@st.cache
def b(text, num_beams, length_penalty, max_length, min_length, no_repeat_ngram_size):
    #build directory
    buildDirectory()
    #build tokenizer
    torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
    text = text.replace('\n','')
    text_input_ids = tokenizer.batch_encode_plus([text], return_tensors='pt', max_length=1024)['input_ids'].to(torch_device)
    summary_ids = model.generate(text_input_ids, num_beams=int(num_beams), length_penalty=float(length_penalty), max_length=int(max_length), min_length=int(min_length), no_repeat_ngram_size=int(no_repeat_ngram_size))           
    summary_txt = tokenizer.decode(summary_ids.squeeze(), skip_special_tokens=True)
    return summary_txt




