from mlflow import log_params, log_metric, log_artifact

if __name__ == "__main__":
    # Log parameters
    log_params({"param1": 5, "param2": 10})

    # Log a metric
    log_metric("accuracy", 0.95)
    log_metric("loss", 0.05)

    # Log an artifact (e.g., a file)
    log_artifact("produced-dataset.csv")


