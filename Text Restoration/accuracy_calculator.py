'''
This code is necessary to count the actual accuracy for both the sentence
boundary and capitalisation tasks. TiMBL's accuracy score is greatly inflated
by the vast number of true negatives that are spotted. This code eliminates
this problem by counting true positives as correct, while it considers false
positives and false negatives wrong.
'''

#Currently set to test sentence boundary accuracy.
f = open("as_test.txt.IB1.O.gr.k1.out", "r")

correct = 0
wrong = 0

#line[-4] refers to the true value whereas line[-2] is the predicted one.

for line in f:
    if line[-4] == '1':
        if line[-2] == '1':
            correct += 1
        else:
            wrong += 1
    else:
        if line[-2] == '1':
            wrong += 1

f.close()

print('True positives:', correct)
print('Sum of false positives and false negatives:', wrong)
print('Accuracy:', correct/(correct + wrong))