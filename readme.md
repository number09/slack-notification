# slack-notification

## これは何？
サーバーレスアプリケーションを Python + Lambda Layer + AWS CDKで構築するサンプルです

### AWSリソース
- Lambda 関数
- Lambda Layer
    - 外部モジュール(今回の場合`requests`)を Lambda Layerにする
- パラメータストア
    - Slackへメッセージを投稿するためのWebhook URLを保存

## 環境構築
`pyenv`,`pipenv`が導入済みであること

```
pipenv install
pipenv install --dev
```

## デプロイ
`awscli`,`awscdk`が導入済みであること  
`cdk bootstrap`を実行済みであること

- `pipenv run layer`
    - `Pipfile`をもとに、Lambda Layer用に外部モジュールを`layer/python`ディレクトリにダウンロード
    - `Pipfile`の`[script]`に定義された`layer`コマンドが実行される
- `cdk deploy slack-notification`
    - CDKでデプロイ

## 実行
マネジメントコンソールのLambdaから直接実行して、Slackにメッセージが送信されることを確認します
