dict1={'b':2,'c':3,'c':4}
dict2 ={'c':5,'a':6,'d':7}
merged_dict={key:dict1.get(key,0)+dict2.get(key,0) for key in set(dict1)| set(dict2)}
print('Merged and Modified Dictionary : ', merged_dict)
