import missingno as msno
import pandas as pd
from scipy.stats import normaltest
from matplotlib import pyplot
from statsmodels.graphics.gofplots import qqplot
import statsmodels.api as sm
import seaborn as sns
import numpy as np


class Plotter:
    def __init__(self, df):
        self.df = df

  
  
    def multiple_histogram_plot(self, num_cols):
        f = pd.melt(self.df, value_vars=num_cols)
        g = sns.FacetGrid(f, col="variable", col_wrap=4,
                          sharex=False, sharey=False)
        g = g.map(sns.histplot, "value", kde=True)
        pyplot.show()

   
    def qq_plot(self, col):
        self.df.sort_values(by=col, ascending=True)
        qq_plot = qqplot(self.df[col], scale=1, line='q')
        pyplot.show()

   
    def multiple_qq_plot(self, cols):
        remainder = 1 if len(cols) % 4 != 0 else 0
        rows = int(len(cols) / 4 + remainder)

        fig, axes = pyplot.subplots(
            ncols=4, nrows=rows, sharex=False, figsize=(12, 6))
        for col, ax in zip(cols, np.ravel(axes)):
            sm.qqplot(self.df[col], line='s', ax=ax, fit=True)
            ax.set_title(f'{col} QQ Plot')
        pyplot.tight_layout()
    
    
    def agostino_k2_test(self, col):
        stat, p = normaltest(self.df[col], nan_policy='omit')
        print('Statistics=%.3f, p=%.3f' % (stat, p))


    def missing_nulls_plot(self):
        msno.matrix(self.df)
        pyplot.show()

  
    def correlated_vars(self, cols):
        corr = self.df[cols].corr()
        mask = np.zeros_like(corr)
        mask[np.triu_indices_from(mask)] = True
        pyplot.figure(figsize=(10, 8))

        cmap = sns.diverging_palette(100, 10, as_cmap=True)

        sns.heatmap(corr, mask=mask, square=True, linewidths=5,
                    annot=False)

        pyplot.show()