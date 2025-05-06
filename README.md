# MLflow Examples Repository

This repository provides practical examples and demonstrations of MLflow usage for machine learning experiment tracking, model management, and deployment.

## Repository Structure

- **Introduction-example/**: Basic introduction to MLflow tracking and metrics
  - `test-mlflow.py`: Simple script for MLflow tracking
  - `produce-metrics.py`: Example script for generating and logging metrics

- **mlflow-demo/**: Complete MLflow workflow demonstration
  - **exploratory/**: Data validation and exploration tools
  - **register/**: Example notebooks for model registration
  - **serve/**: Sample code for model serving and deployment

## Quick Start

1. Install dependencies:
   ```
   pip install mlflow pandas scikit-learn
   ```

2. Run an example:
   ```
   cd Introduction-example
   python test-mlflow.py
   ```

3. View your results:
   ```
   mlflow ui
   ```
   Then open http://localhost:5000 in your browser

## Key Features

- Experiment tracking with metrics, parameters, and artifacts
- Model versioning and registration
- Model deployment examples
- Integration with various ML frameworks

## Requirements

- Python 3.6+
- MLflow
- Additional dependencies in respective directory requirements files