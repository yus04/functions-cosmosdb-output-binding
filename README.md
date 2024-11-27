# functions-cosmosdb-output-binding
Python をランタイムとした Azure Functions に関して、 Cosmos DB の output binding のサンプル例です。

## 前提条件
- Azure Functions がデプロイ済みであること
- Azure Blob Storage がデプロイ済みであること
- Azure Cosmos DB がデプロイ済みであること
- Azure Cosmos DB に my-database のデータベースと、my-container のコンテナが、id をパーティションキーとして設定されていること
- Functions Core Tool がインストール済みであること (ローカル実行の場合)

## 設定・実行手順
### ローカル実行の場合
- local.settings.json の Values に以下のパラメーターを設定
    - AzureWebJobsStorage
    - CosmosDbConnectionSetting
- Visual Studio Code であれば、F5 によりローカルで Functions を実行
- ブラウザにて、http://localhost:7071/api/http_trigger?name=\<your-name> をリクエスト
- Azure Cosmos DB に your-name が登録されていることを確認

### Azure 実行の場合
- Visual Studio Code などを使い、Azure Functions にコードをデプロイする
- Azure Functions の環境変数に、以下のパラメーターを設定
    - CosmosDbConnectionSetting
- ブラウザにて、<Azure Functions の URL>/api/http_trigger?name=\<your-name> をリクエスト
- Azure Cosmos DB に your-name が登録されていることを確認

## 参考文献
- Visual Studio Code を使用して Azure Functions を Azure Cosmos DB に接続する
    - https://learn.microsoft.com/ja-jp/azure/azure-functions/functions-add-output-binding-cosmos-db-vs-code?pivots=programming-language-python
- Azure Functions 2.x 以降に対する Azure Cosmos DB の出力バインド
    - https://learn.microsoft.com/ja-jp/azure/azure-functions/functions-bindings-cosmosdb-v2-output?tabs=python-v2%2Cisolated-process%2Cnodejs-v4%2Cextensionv4&pivots=programming-language-python#example