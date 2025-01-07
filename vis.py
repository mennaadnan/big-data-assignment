import seaborn as sns
import matplotlib.pyplot as plt

def visualization(df):
    # Generate the heatmap
    sns.heatmap(df.corr(), annot=True)
    plt.savefig("vis.png")  # Save the heatmap visualization
    
    # Now, pass the data to the next step (modeling)
    from model import kmeans
    kmeans(df)  # Pass the data for KMeans clustering
