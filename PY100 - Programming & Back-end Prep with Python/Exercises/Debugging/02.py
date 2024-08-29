'''
Weather Forecast

Our predict_weather function should output a message indicating whether a sunny
or cloudy day lies ahead. However, the output is the same every time the
function is invoked. Why? Fix the code so that it behaves as expected.

import random

def predict_weather():
    sunshine = random.choice(['True', 'False'])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")
'''


'''
The output is the same every time because sunshine is always 'True' or 'False',
which are not the boolean values True and False but the strings 'True' and
'False'. Non-empty strings are truthy in value, so the if statement is always
True.
'''


import random

def predict_weather():
    sunshine = random.choice([True, False])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

predict_weather()
