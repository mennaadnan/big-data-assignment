import seaborn as sns
import matplotlib.pyplot as plt

def visualization(df):
    # Generate the heatmap
    sns.heatmap(df.corr(), annot=True)
    plt.savefig("vis.png")
    
    #pass the data to the next step
    from model import kmeans
    kmeans(df) 
