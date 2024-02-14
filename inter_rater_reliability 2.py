import pandas as pd
from sklearn.metrics import cohen_kappa_score

df = pd.read_excel("all rater 1 and 2.xlsx")
# Index(['Column1', 'Element:Text1', 'Attribute:id',
#        'Attribute:features (RATER 1)', 'Table.Attribute:features (RATER 2)'],
#       dtype='object')
# assuming your data is in the following format
# rater1 = [
#     ["abstract_analysis", "introduction", "aim"],
#     ["abstract_analysis", "introduction", "defining"],
# ]
# rater2 = [
#     ["abstract_analysis", "introduction", "defining"],
#     ["introduction", "abstract_analysis", "aim"],
# ]
rater1 = []
rater2 = []
for _, row in df.iterrows():
    if type(row["Attribute:id"]) == str and "Attribute:id" in row["Attribute:id"]:
        continue
    rater1.append(row["Attribute:features (RATER 1)"].split(";"))
    rater2.append(row["Table.Attribute:features (RATER 2)"].split(";"))
rater1_list = []
rater2_list = []
for r1, r2 in zip(rater1, rater2):
    new_r1 = []
    new_r2 = []
    unique_features = set(r1+r2)
    not_in_both = []
    for f in unique_features:
        if f in r1 and f in r2:
            new_r1.append(f)
            new_r2.append(f)
        else:
            not_in_both.append(f)
    for f in not_in_both:
        if f in r1:
            new_r1.append(f)
        else:
            new_r2.append(f)
    while len(new_r1) < len(new_r2):
        new_r1.append("None")
    while len(new_r2) < len(new_r1):
        new_r2.append("None")
    rater1_list.extend(new_r1)
    rater2_list.extend(new_r2)

# calculate Cohen's Kappa
kappa = cohen_kappa_score(rater1_list, rater2_list)
print("Cohen's Kappa: ", kappa)
