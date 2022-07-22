# -*- coding: utf-8 -*-
"""customer_segmentation_module.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yl8v2bXAuyDicsnaL-3_-yO9TdkKh6K9
"""

#%% Libraries

from tensorflow.keras.layers import Dense,Dropout,BatchNormalization
from tensorflow.keras import Sequential, Input
import matplotlib.pyplot as plt 
import scipy.stats as ss
import seaborn as sns 
import numpy as np

#%% SNS Plots

class EDA:
  def displot_graph(con_col,df,color='c'):
      '''
      This function is meant to plot continuos data using seaborn distplot function

      Parameters
      ----------
      con_col : LIST
          con_col contains the name of the categorical columns.
      df : DATAFRAME
          dataframe to plot
      c : STR, optional
          String that sets the colour of the plot

      Returns
      -------
      None.
      '''
      for i in con_col:
          plt.figure()
          sns.distplot(df[i],color=color)
          plt.show()

  def countplot_graph(cat_col,df,palette='pastel'):
      '''
      This function is meant to plot categorical data using seaborn countplot function

      Parameters
      ----------
      cat_col : LIST
          cat_col contains the name of the categorical columns.
      df : DATAFRAME
          dataframe to plot
      c : STR, optional
          String that sets the palette of the plot. Default is pastel.

      Returns
      -------
      None.
      '''

      for i in cat_col:
          plt.figure()
          sns.countplot(df[i],palette=palette)
          plt.show()

#%% Cramers Function

def cramers_corrected_stat(confusion_matrix):
    """ calculate Cramers V statistic for categorial-categorial association.
        uses correction from Bergsma and Wicher,
        Journal of the Korean Statistical Society 42 (2013): 323-328
    """
    chi2 = ss.chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum()
    phi2 = chi2/n
    r,k = confusion_matrix.shape
    phi2corr = max(0, phi2 - ((k-1)*(r-1))/(n-1))  
    rcorr = r - ((r-1)**2)/(n-1)
    kcorr = k - ((k-1)**2)/(n-1)
    return np.sqrt(phi2corr / min( (kcorr-1), (rcorr-1)))

#%% DL Model Developement
class MODEL:
    def nn_model(self, input_shape,nb_class,nb_node=64,dropout_rate=0.3):
        '''
        A 3 layers neural network model with 'relu' as activation function.

        Parameters
        ----------
        input_shape : SERIES
            shape of X train
        nb_class : INT
            number of categories of the target
        nb_node : INT, optional
            number of nodes, usually in the power of 2. Default is 64.
        dropout_rate : FLOAT, optional
            DESCRIPTION. The default is 0.3.

        Returns
        -------
        None.
        '''
        model=Sequential()
        model.add(Input(shape=input_shape))
        model.add(Dense(nb_node,activation='relu'))
        model.add(BatchNormalization())
        model.add(Dropout(dropout_rate))
        model.add(Dense(nb_node,activation='relu'))
        model.add(BatchNormalization())
        model.add(Dropout(dropout_rate))
        model.add(Dense(nb_node,activation='relu'))
        model.add(BatchNormalization())
        model.add(Dropout(dropout_rate))
        model.add(Dense(nb_class,activation='softmax'))
        model.summary()
        
        return model

#%% Model Evaluation
class ModelEvaluation():
    def LOSS_plot(self,hist):
        plt.figure()
        plt.plot(hist.history['loss'])
        plt.plot(hist.history['val_loss'])
        plt.legend(['Training Loss', 'Validation Loss'])
        plt.show()
    
    def ACC_plot(self,hist): 
        plt.figure()
        plt.plot(hist.history['acc'])
        plt.plot(hist.history['val_acc'])
        plt.legend(['Training Accuracy', 'Validation Accuracy'])
        plt.show()