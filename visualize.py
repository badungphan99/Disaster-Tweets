import matplotlib.pyplot as plt
import seaborn as sns

class vis:
    def targetDistribution(data):
        fig, axes = plt.subplots(ncols=2, nrows=1, figsize=(18, 6))
        sns.countplot(data['target'], ax=axes[0])
        axes[1].pie(data['target'].value_counts(),
                    labels=['Not Disaster', 'Disaster'],
                    autopct='%1.2f%%',
                    shadow=True,
                    explode=(0.05, 0),
                    startangle=60)
        fig.suptitle('Distribution of the Tweets', fontsize=24)
        plt.savefig('images/DistributionoftheTweets.png')