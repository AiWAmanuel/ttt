libraries = [
    # Core Libraries for Numerical and Statistical Analysis
    "numpy", "pandas", "scipy", "statsmodels",

    # Data Visualization
    "matplotlib", "seaborn", "plotly", "bokeh", 
    "altair", "ggplot", "dash",

    # Machine Learning
    "sklearn", "xgboost", "lightgbm", "catboost", 
    "tensorflow", "torch", "keras",

    # Data Cleaning and Preprocessing
    "openpyxl", "pyjanitor", "missingno", 
    "dask", "polars",

    # Big Data and Distributed Computing
    "pyspark", "vaex",

    # Time Series Analysis
    "prophet", "pycaret",

    # Deep Learning
    "fastai",

    # Data Engineering and ETL
    "sqlalchemy", "pyarrow", "apache_beam", 
    "pandas_profiling", "great_expectations",

    # Deployment and Integration
    "flask", "fastapi", "streamlit", "gradio",

    # Miscellaneous Tools
    "tqdm", "joblib", "pydantic"
]

for lib in libraries:
    try:
        __import__(lib)
        print(f"Successfully imported {lib}")
    except ImportError as e:
        print(f"Failed to import {lib}. Error: {e}")
