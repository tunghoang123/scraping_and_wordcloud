## scraping_and_wordcloud
recsys2023の論文のタイトルからwordcloudを作成する。

## 参考
https://note.com/shi3zblog/n/n7eaba88ffe4a

## 補足
単純にseleniumを使ってタイトルを取得しても良いが、せっかくなので上記記事のOpen Interpreterを使ってみる。

### Open Interpreter
```
# インストール
$ pip install open-interpreter  
# python3.10系でインストールできるっぽい

# 起動
$ export OPENAI_API_KEY=xxxxxxxxx
$ interpreter -y


```