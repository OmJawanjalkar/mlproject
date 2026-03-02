# Student Performance Prediction

Machine learning project to predict student math scores based on demographic and academic factors.

## Tech Stack

- Python 3.10
- scikit-learn, CatBoost, XGBoost
- Flask
- Pandas, NumPy

## Installation

```bash
# Clone repository
git clone <repository-url>
cd mlproject

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -e .
```

## Usage

### Run Web App
```bash
python app.py
```
Access at `http://localhost:5000`

## Features

- **Data Pipeline**: Automated data ingestion, transformation, and splitting
- **Model Training**: Multiple algorithms with hyperparameter tuning via GridSearchCV
- **Web Interface**: Flask app for predictions
- **Deployment**: AWS Elastic Beanstalk & Azure Web Apps support

## Project Structure

```
mlproject/
├── artifacts/          # Trained models and data
├── src/
│   ├── components/     # Data ingestion, transformation, model training
│   ├── pipeline/       # Prediction pipeline
│   └── utils.py        # Helper functions
├── templates/          # HTML files
├── app.py             # Flask application
└── requirements.txt
```

## Models Used

- Random Forest
- Gradient Boosting
- XGBoost
- CatBoost (Best performer)
- Linear Regression
- Decision Tree
- AdaBoost

## API Endpoints

- `GET /` - Home page
- `GET /predictdata` - Prediction form
- `POST /predictdata` - Make prediction

## Input Features

- Gender
- Race/Ethnicity
- Parental Education Level
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score