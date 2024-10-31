nested_dict={
    'person':{
        'name':'Mahabur',
        'details':{
            'age':26,
            'city':'Dhaka',
            'skills':['Python','Data Analysis']
        }
    }
}
city =nested_dict['person']['details']['city']
nested_dict['person']['details']['skills'].append('Machine Learning')
print('City :',city)
print('Update Nested Dictionary : ', nested_dict)


