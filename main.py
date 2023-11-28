# 出力先のデータベース (SQLite3)
save_db_path = "out.db"

# 対象のYouTube動画のURL
videos = [
    "https://www.youtube.com/watch?v=ieMKBctJ2aM"
]

###################################

from faster_whisper import WhisperModel
import torch
import tempfile
from youtube import download_video_from_youtube
from db import Database

# GPUが使える場合はGPUを使う
if not torch.cuda.is_available():
    print("Warning: CUDA is not available. The model will run on CPU.")

print(">> Loading speech to text model...")
# 大規模モデルを読み込む
whisper_model = WhisperModel("large-v2", device="cuda", compute_type="int8_float16")
print("<< Loaded speech to text model\n")

# データベースインスタンスを作り、データベースに接続する
db = Database(save_db_path)

for video in videos:
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f">> Downloading video: {video}")

        # YouTubeから動画をダウンロードする
        video_path, video_id, video_title = download_video_from_youtube(video, temp_dir)
        if not video_path:
            continue

        print(f"   Downloaded video: {video_title} ({video_path})")

        # 動画から文字起こしをする
        segments, info = whisper_model.transcribe(
            video_path,
            language="ja"
        )

        # 動画情報を格納
        try:
          db.insert_yt_video_no_commit(
              video_id,
              video_title
          )
        except Exception as e:
          print(e)
          print("<< Skipped")
          continue

        # 文字起こし結果を格納
        for segment in segments:
            db.insert_talk_no_commit(
                video_id,
                int(segment.start),
                int(segment.end),
                segment.text
            )

        # データベースに反映
        db.commit()

        print("<< Transcribed video\n")

# データベースと切断する
db.close()
