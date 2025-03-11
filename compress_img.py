from dotenv import load_dotenv
import os
import tinify

# .envファイルを読み込む
load_dotenv()

# TinyPNGのAPIキーを設定
tinify.key = os.getenv("TINIFY_API_KEY")

# フォルダのパスを定義
original_folder = os.path.join(os.getcwd(), 'original')
images_folder = os.path.join(os.getcwd(), 'img')

# imagesフォルダが存在しない場合は作成
os.makedirs(images_folder, exist_ok=True)

# originalフォルダ内の全ての画像を圧縮
for filename in os.listdir(original_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        source_path = os.path.join(original_folder, filename)
        target_path = os.path.join(images_folder, filename)

        try:
            source = tinify.from_file(source_path)
            source.to_file(target_path)
            print(f"{filename} を圧縮して保存しました。")
        except tinify.Error as e:
            print(f"エラー: {filename} の圧縮に失敗しました -> {e}")

print("全ての画像の圧縮が完了しました。")
