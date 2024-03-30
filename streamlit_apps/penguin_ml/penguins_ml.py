import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

pennguin_df = pd.read_csv("penguins.csv")
pennguin_df.dropna(inplace=True)
output = pennguin_df["species"]
features = pennguin_df[[
    "island", "bill_length_mm", "bill_depth_mm",
    "flipper_length_mm", "body_mass_g", "sex"]]

features = pd.get_dummies(features, drop_first=True, dtype=int)

output, uniques = pd.factorize(output)

X_train, X_test, y_train, y_test = train_test_split(
        features, output, test_size=0.8, random_state=15
    )

rfc = RandomForestClassifier(random_state=15)

rfc.fit(X_train.values, y_train)

y_pred = rfc.predict(X_test.values)

score = accuracy_score(y_pred, y_test)


print('Our accuracy score for this model is {}'.format(score))

rf_pickle = open("random_forest_penguin.pickle", "wb")
pickle.dump(rfc, rf_pickle)
rf_pickle.close()
output_pickle = open("output_penguin.pickle", "wb")
pickle.dump(uniques, output_pickle)
output_pickle.close()