
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

class Main:
    def __init__(self):
        self.data = pd.read_csv("http://pythondatascience.plavox.info/wp-content/uploads/2016/05/Wholesale_customers_data.csv")
        self.Pdata = []
        self.ansdata = []
        self.cl = 0

    def fit(self, x):
        self.cl = x
        del(self.data['Channel'])
        del(self.data['Region'])
        self.Pdata = np.array([self.data['Fresh'].tolist(),
                               self.data['Milk'].tolist(),
                               self.data['Grocery'].tolist(),
                               self.data['Frozen'].tolist(),
                               self.data['Milk'].tolist(),
                               self.data['Detergents_Paper'].tolist(),
                               self.data['Delicassen'].tolist()
                               ], np.int32)
    def ans(self):
        Tdata = self.Pdata.T
        self.ansdata = KMeans(n_clusters=self.cl).fit_predict(Tdata)
        self.data['cluster_id']=self.ansdata

    def dataget(self):
        print self.data['cluster_id'].value_counts()
        for i in range(self.cl):
            print "======================================="
            print "classNumber is " + str(i)
            print self.data[self.data['cluster_id']==i].mean()
            print "======================================="

    def dataplot(self):
        import matplotlib.pyplot as plt
        clusterinfo = pd.DataFrame()
        for i in range(self.cl):
            clusterinfo['cluster' + str(i)] = self.data[self.data['cluster_id'] == i].mean()
        clusterinfo = clusterinfo.drop('cluster_id')
        my_plot = clusterinfo.T.plot(kind='bar', stacked=True, title="Mean Value of " + str(self.cl) + " Clusters")
        my_plot.set_xticklabels(my_plot.xaxis.get_majorticklabels(), rotation=0)
        plt.show()

    def dendoplot(self):
        from  scipy.spatial.distance  import pdist
        from scipy.cluster.hierarchy import linkage, dendrogram
        import matplotlib.pyplot as plt

        pdist = pdist((self.data))
        result = linkage(pdist)
        dendrogram(result)
        plt.show()

def main():
    CK = Main()
    CK.fit(4)
    CK.ans()
    CK.dataplot()
    CK.dendoplot()
    CK = None

if __name__=="__main__":
    main()
