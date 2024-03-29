import mlflow
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor

mlflow.set_tracking_uri("http://localhost:5001")

with mlflow.start_run(run_name=f'random_forest_{str(datetime.now().date())}') as run:
    mlflow.autolog()

    db = load_diabetes()
    X_train, X_test, y_train, y_test = train_test_split(db.data, db.target, test_size=0.25, train_size=0.75, random_state=2)

    # Create and train models.
    rf = RandomForestRegressor(n_estimators=100, max_depth=6, max_features=3)
    rf.fit(X_train, y_train)

    # Use the model to make predictions on the test dataset.
    predictions = rf.predict(X_test)

    runid = run.info.run_id
    print(runid)
