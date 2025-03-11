compress_img
概要
このプロジェクトは、画像圧縮スクリプトを提供します。主にTinify（TinyPNG）のAPIを利用して、指定されたディレクトリ内の画像を圧縮します。

新機能

✅ パスの指定をより安全に

✅ APIキーを環境変数に保存し、セキュリティ強化

✅ エラーハンドリングで失敗を検知

✅ 進捗表示を追加して実行状態が分かるように

必要な準備

1. Tinify APIキーの取得

このスクリプトはTinyPNGのAPIを使用して画像を圧縮します。以下のリンクからAPIキーを取得してください。

Tinify APIキーの取得

アカウント登録後、すぐにAPIキーが取得できます。

**インストール手順**

1. リポジトリをクローン

GitHubなどのリモートリポジトリからプロジェクトをクローンし、プロジェクトディレクトリに移動します。

(bash)
git clone <リポジトリのURL>

cd <プロジェクトディレクトリ>


2. 仮想環境の作成と有効化

依存関係をインストールするために仮想環境を作成し、有効化します。

macOS/Linuxの場合：

(bash)

python3 -m venv myproject-env

source myproject-env/bin/activate

Windowsの場合：

(bash)

python -m venv myproject-env

myproject-env\Scripts\activate

3. 依存パッケージのインストール

requirements.txtがある場合は、以下のコマンドで必要なパッケージをインストールします。

(bash)

pip install -r requirements.txt

または、手動で必要なパッケージをインストールする場合：

(bash)

pip install python-dotenv tinify

4. 環境変数の設定

プロジェクトのルートディレクトリに .env ファイルを作成し、以下の内容を追加します。TINIFY_API_KEY には実際のAPIキーを設定してください。

TINIFY_API_KEY=your_api_key_here

注意: your_api_key_here は、取得した自分のAPIキーに置き換えてください。

5. 動作確認
インストール後、仮想環境内で以下のコマンドを実行し、動作確認を行います。

(bash)

python compress_img.py

圧縮が正常に動作すれば、準備完了です。

操作方法

1. 画像の圧縮

compress_img.py を実行することで、指定されたディレクトリ内の画像が圧縮されます。

(bash)

python compress_img.py

このスクリプトは、指定された画像ファイルをTinify APIを使用して圧縮し、圧縮後の画像を保存します。

エラー処理

APIキーが正しく設定されていない場合:

.env ファイルに設定した TINIFY_API_KEY が正しいかを確認してください。設定が正しくないと、エラーが発生します。

画像の圧縮に失敗した場合:
圧縮対象の画像ファイルのパスが間違っているか、APIの制限に達している可能性があります。エラーメッセージが表示されるので、それに従って修正してください。

