# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df=pd.read_csv(path)
p_a = df[df['fico']>700].shape[0]/df.shape[0]
print('Probability for the event that fico credit score is greater than 700 is: ',p_a)

p_b = df[df['purpose'] == 'debt_consolidation'].shape[0]/df.shape[0]
print('probability for the event that purpose is debt_consolation is: ',p_b)

df1=df[(df['purpose'] == 'debt_consolidation')&(df['fico']>700)]

p_a_b = (df1.shape[0]/df.shape[0])/p_a
print('The probablity for the event purpose is debt_consolidation given fico credit score is greater than 700 is: ',p_a_b)

if p_a_b==p_a:
    result = True
else:
    result = False

print('Result is: ',result)
# code ends here


# --------------
# code starts here
prob_lp = df[df['paid.back.loan']=='Yes'].shape[0] / lengthOfDf
print('The probability for the event that paid.back.loan = Yes is: ',prob_lp)

prob_cs = df[df['credit.policy']=='Yes'].shape[0] / lengthOfDf
print('The probability for the event that credit.policy = Yes is: ',prob_cs)

new_df = df[df['paid.back.loan'] == 'Yes']

prob_pd_cs = new_df[new_df['credit.policy'] == 'Yes'].shape[0] / new_df.shape[0]
print('The event paid.back.loan = Yes given credit.policy = Yes is: ',prob_pd_cs)

bayes = (prob_pd_cs*prob_lp)/prob_cs
print('Bayes is: ',bayes)
# code ends here


# --------------
# code starts here
df1 = df[df['paid.back.loan'] == 'No']
df1.plot.bar()
plt.show()
# code ends here


# --------------
# code starts here
inst_median = df['installment'].median()
print('Median for the installment is: ',inst_median)

inst_mean = df['installment'].mean()
print('Mean for the installment is: ',inst_mean)

df['installment'].hist()

df['log.annual.inc'].hist()

# code ends here


