from msilib import sequence
from tkinter import Scale
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('dna.jfif')

st.image(image.resize([160, 200]))

st.write("""
         
         #DNA Nucleotide Count Web App
         
         This app counts the nucleoide composition og query DNA
         
         """)

st.header("Enter DNA sequence")

sequence_input = ">DNA Query\n GGAACCCCTCGAAATTCCTCGATCGATGCTAGCTGACTGACTGATGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGACTAGCTACGAC\nTGAGGTGTATCAGCTGCTGATGCTGGGGCATCGATGCGGCATTAGCGGAACCCCTCGATCGATCGATGCTAGCTGACTGACTGATGACTGAGCTAGCGAC\nTGAGGTGTATCAGCTGCTGATGCTGGGGCATCGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAATGCGGCATTAGC"

sequence = st.text_area("Sequense Input", sequence_input, height=30)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("""***""")

st.header('Input (DNA Query)')
sequence

st.header('Output (DNA Nucleotide Count)')

st.subheader('1. Print dictionay')
def dna_nucleotidecout(seq):
    d = dict([
            ('A', seq.count('A')),
            ('T', seq.count('T')),
            ('G', seq.count('G')),
            ('C', seq.count('C')),
    ])
    
    return d
    
X = dna_nucleotidecout(sequence)


X


st.subheader('2. Print text')
st.write('There are ' + str(X['A']) + ' andenine (A)')
st.write('There are ' + str(X['T']) + ' thenine (T)')
st.write('There are ' + str(X['G']) + ' guanine (G)')
st.write('There are ' + str(X['C']) + ' cytosine (C)')



st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index' : 'nucleotide'})
st.write(df)

st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p.properties(
    width=alt.Step(95)
)

st.write(p)