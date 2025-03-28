# scrappin_amazon

Using beautiful soup in python to retrive information about a product listing on amazon, through the title of the listing on the page.
We will be using beautiful soup to scrape product information and save the details in a CSV file. Finally, applying machine learning models to predict product prices based on extracted features.

### Features Extracted

- Product Title
- Brand Name (extracted from title)
- Average Rating
- Review Count
- Price

### Machine Learning Models Used

- Random Forest Regressor
- XGBoost Regressor

## How to Run the Project

1. Install Dependencies

- Ensure you have the required Python libraries installed:

- pip install requests beautifulsoup4 pandas scikit-learn xgboost

2. Run the Scraper

- Execute the scraper script to collect data:

- python scraper.py

- This will save the scraped data as scraped_amazon_data.csv.

3. Train the Machine Learning Model

- Run the Jupyter Notebook (Scraping_Amazon_ML.ipynb) to process data, extract features, and train models:

- jupyter notebook Scraping_Amazon_ML.ipynb

### Evaluation Metrics

- Mean Absolute Error (MAE)

- Root Mean Squared Error (RMSE)

### Future Improvements

- Add deep learning models for price prediction.

- Deploy as a web app for real-time predictions.

-Automate data scraping using Selenium.

