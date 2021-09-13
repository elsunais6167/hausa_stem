#install libararies
#pip install hausastemmer
#pip install pandas

#importing Bimba's Algorithsm
import hausastemmer as bimba

#importing Suraj's Improved Algorithsm 
from improved.HausaStemmer import HausaStemmer 

#import pandas dataframe library
import pandas as pd

#Using pandas to import dataset containing Normal Words and Already Stemmed Words
data = pd.read_csv('test_words.csv')
actual = data.actual_words
expected = data.expected_stem
print(data)

#Calling Suraj's improved algorithms
suraj = HausaStemmer()

#looping through the Actual words columns to read data
for  item in data.actual_words:
    #using suraj's improved algorithsm to stem words with the improved lookup words
    suraj_algo = suraj.stem(item, lookup=True)
    
    #using bimba's algorithsm to stem words with bimba's lookup words
    bimba_algo = bimba.stem(item, lookup=True)

    #-------exporting the stem output and merge with initial words--------

    # out_put = pd.DataFrame({'Actual_Words': actual, 'Expected_Stem': expected, 'Suraj_Algorithsm': suraj_algo, 'Bimba_Algorithsm': bimba_algo})
    # out_put.to_csv('stem_output.csv')

#reading the exported stemmmed words output file
stem_data = pd.read_csv('stem_output.csv')
print(stem_data)

#comparing both Bimba's algorithsm and Suraj's improved algorithsm with expected_stem 
stem_data["Surajs_Correct_Stemming"] = (stem_data['Expected_Stem']==stem_data['Suraj_Algorithsm'])
stem_data["Bimbas_Correct_Stemming"] = (stem_data['Expected_Stem']==stem_data['Bimba_Algorithsm'])
print(stem_data)

#counting correct stemmed words with Suraj's Improved Algorithsm 
surajs_correct_stemmed_words = stem_data['Surajs_Correct_Stemming'].value_counts()
print(surajs_correct_stemmed_words)

#"True" means correctly stemmed
#"False" means wrongly stemmed

#counting correct stemmed words with Bimba's Improved Algorithsm 
bimbas_correct_stemmed_words = stem_data['Bimbas_Correct_Stemming'].value_counts()
print(bimbas_correct_stemmed_words)

#"True" means correctly stemmed
#"False" means wrongly stemmed