import mlflow

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

mlflow.set_tracking_uri("http://localhost:5001")

def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2


db = load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(db.data, db.target)

logged_model = 'runs:/8375026ea1504776bf6da47d073936a5/model'

model = mlflow.sklearn.load_model(logged_model)
predictions = model.predict(X_test)
print(predictions)

(rmse, mae, r2) = eval_metrics(y_test, predictions)

print("  RMSE: %s" % rmse)
print("  MAE: %s" % mae)
print("  R2: %s" % r2)
