import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

penguin_df = pd.read_csv("streamlit_apps/penguin_ml/penguins.csv")
penguin_df.dropna(inplace=True)
output = penguin_df["species"]
features = penguin_df[[
    "island", "bill_length_mm", "bill_depth_mm",
    "flipper_length_mm", "body_mass_g", "sex"]]

features = pd.get_dummies(features, drop_first=True, dtype=int)

print(f"Features: {features}")

output, uniques = pd.factorize(output)

X_train, X_test, y_train, y_test = train_test_split(
        features, output, test_size=0.8, random_state=15
    )

rfc = RandomForestClassifier(random_state=15)

rfc.fit(X_train.values, y_train)

y_pred = rfc.predict(X_test.values)

score = accuracy_score(y_pred, y_test)


print('Our accuracy score for this model is {}'.format(score))

rf_pickle = open("streamlit_apps/penguin_ml/random_forest_penguin.pickle", "wb")
pickle.dump(rfc, rf_pickle)
rf_pickle.close()
output_pickle = open("streamlit_apps/penguin_ml/output_penguin.pickle", "wb")
pickle.dump(uniques, output_pickle)
output_pickle.close()

fig, ax = plt.subplots()
ax = sns.barplot(x=rfc.feature_importances_, y=features.columns)
fig.suptitle('Which features are the most important for species prediction?', ha='center')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.tight_layout()

fig.savefig('streamlit_apps/penguin_ml/feature_importance.png')