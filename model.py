from sklearn.cluster import KMeans

def kmeans(df):
    X = df
    y = df['Customer Status']
    
    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=3, random_state=0)
    kmeans.fit(X)
    
    # Get the cluster labels and count the number of records in each cluster
    labels = kmeans.labels_
    cluster_count = 1
    text = ""
    for label in set(labels):
        count = len([x for x in labels if x == label])
        text += f"Cluster {cluster_count}: {count} data points\n"
        cluster_count += 1
    
    # Save the cluster counts to k.txt
    with open("k.txt", "w") as f:
        f.write(text)

    print("Pipeline Finished! Run final.sh to transfer data and close the container.")
