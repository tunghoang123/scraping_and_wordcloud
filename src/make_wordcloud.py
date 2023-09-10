# -*- coding: utf-8 -*-
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd


def main():
    df = pd.read_csv('../data/recsys23_data.tsv', sep='\t')
    titles = df['title'].tolist()
    wc = WordCloud(background_color='white', max_words=40, colormap="tab20b").generate(' '.join(titles))
    plt.imshow(wc)
    plt.savefig("wordcloud.png")


if __name__ == '__main__':
    main()
