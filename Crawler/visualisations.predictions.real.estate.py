import numpy as np
import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plot
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn import datasets
from sklearn.model_selection import train_test_split

if __name__ == '__main__':

    # my code

    dataframe = pd.read_csv('data/fully_processed_nsw_dataset.csv')     # dataset in whole
    input_df = pd.read_csv('data/fully_processed_nsw_dataset_input.csv')
    output_df = pd.read_csv('data/fully_processed_and_mapped_nsw.csv')  # dataframe with mapped TYPE
    nsw_x = input_df.values.__array__()                                 #
    nsw_y = output_df['Type'].values.__array__()                        # type

    nsw_target_names = np.unique(dataframe['Type'])
    nsw_feature_names = input_df.columns.values
    nsw_number_classes = len(nsw_target_names)
    nsw_number_features = len(nsw_feature_names)

    #print(nsw_target_names)

    colors = ['navy', 'turquoise', 'darkorange', 'black', 'magenta', 'cyan', 'yellow']

    #Visualisations

    fig = plot.figure(figsize=(10, 15))
    fig.subplots(nrows=2, ncols=2)
    for feat in range(nsw_number_features):
        ax = plot.subplot(3, 2, feat + 1)
        plot.title(nsw_feature_names[feat])
        sns.distplot(nsw_x[:, feat])
        for class_type in range(nsw_number_classes):
            sns.distplot(nsw_x[nsw_y == class_type, feat], color=colors[class_type], label=nsw_target_names[class_type])
        plot.legend()
    plot.show()
    

    fig = plot.figure(figsize=(10, 10))
    plot.title("Scatterplots of the NSW dataset features")
    fig.subplots(nrows=5, ncols=5)
    for featOne in range(nsw_number_features):
        for featTwo in range(nsw_number_features):
            ax = plot.subplot(5, 5, nsw_number_features * featOne + featTwo + 1)
            for color, i, target in zip(colors, [0, 1, 2, 3, 4, 5, 6], nsw_target_names):
                plot.scatter(nsw_x[nsw_y == i, featOne], nsw_x[nsw_y == i, featTwo],alpha=.8, color = color)
            plot.xticks()
            plot.yticks()
            plot.title("Feature" + str(featOne) + " x Feature" + str(featTwo))
    plot.show()


    #Prediction

    """
    
    nsw_x_train, nsw_x_test, nsw_y_train, nsw_y_test = train_test_split(nsw_x, nsw_y, test_size=0.22)

    gnb = GaussianNB()
    mnb =  MultinomialNB()
    
    gnb.fit(nsw_x_train, nsw_y_train)
    mnb.fit(nsw_x_train, nsw_y_train)
    
    gaussian_nsw_y_prediction = gnb.predict(nsw_x_test)
    multinomial_new_y_prediction = mnb.predict(nsw_x_test)
    #print(nsw_y_prediction)
    gaussian_accuracy = np.round(np.sum(nsw_y_test == gaussian_nsw_y_prediction)/len(nsw_y_test), 3)
    multinomial_accuracy = np.round(np.sum(nsw_y_test == multinomial_new_y_prediction) / len(nsw_y_test), 3)
    print(dataframe['Address Locality'])
    
    """