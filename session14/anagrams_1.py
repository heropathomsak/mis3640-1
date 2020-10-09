"""
Pseudo-code:

1. read the file, save the words into a list

2. sort word
'anna' -> 'aann' (signature of the word)
'nana' -> 'aann'

3. create a dict, the key is the signature,
value is a list of words that have the same signature

{'aann': ['anna', 'nana'], 'iq' : ['qi']}

4. get the values from the dict, only those lists with more than one item



5. create a dict like below

{6: ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled'],

3: ['resmelts', 'smelters', 'termless'],

2: ['retainers', 'ternaries'],

2: ['generating', 'greatening'],}



"""
