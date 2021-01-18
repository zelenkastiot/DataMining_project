**Летен семестар, 2020** <br> <br>

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1nentTqUAL32LIOe2nJ8y5Zuif-Ge4bsM?usp=sharing)

**Project** 

- **Mentors**: Жанета Попеска, Билјана Тојтовска, Бојан Иљиоски
- **Students:** Давид Ордевски, Кирил Зеленковски 
- **Content:** Reproducible Colab notebook for a short research project related to real estate data, housing prices, and the features that go inside datasets that contain these sorts of data. In this notebook, we will see different regression methods and how well do they predict on our dataset, together with methods like:
          <ul><li><b>Data transformation</b></li>
          <li><b>Label and Ordinal Encoding</b></li>
          <li><b>Handling missing values</b></li>
          <li><b>Getting Dummy Variables</b></li>
          <li><b>Feature Selection</b></li></ul>
The dataset used is from Kaggle, named [Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques). With the implementation of different preprocessing technics and machine learning models in Python, we will see how accurate these methods predict the sale price, both for the scraped dataset and in the Kaggle dataset. The project is primarily divided into 3 parts: 
  1. <u><b>First part: </b></u> Preprocessing, cleaning and training models on the **Kaggle**; [dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)  
    - RidgeCV, LassoCV, BayesianRidge, LinearRegression, XGBRegressor, Neural Network
  2. <u><b>Second part: </b></u> Scraping a dataset using a custom <code>web-crawling</code> script for the site [domain.com.au](https://www.domain.com.au/)  
  3. <u><b>Third part: </b></u> Cleaning and mapping to ordinal values on the scraped dataset, training different models 
    - Categorical Naive Bayes, Decission Tree Classifier, Random Forrest Classifier, Logistic Regression
- **Key words**: Python, Plotly, Data Mining, Web-crawler, Feature Selection, Linear Regression
- **Presentation**: Accesiable on *Google Slides*, [here](https://drive.google.com/file/d/1OK9SD2_eXIVwd-gnryWhj9Nqls7pg9xP/view?usp=sharing)
- **Jupyter notebook**: Nbviewer for better view of the notebook, [here](https://nbviewer.jupyter.org/github/zelenkastiot/FCSE-Data-Mining/blob/master/Notebook/DataMining.ipynb)
