from yt_dlp import YoutubeDL
import os
from typing import Optional

def download_video_from_youtube(
    video_url: str,
    save_dir: str
) -> Optional[tuple[str, str, str]]:

    options = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(save_dir, "%(id)s.%(ext)s")
    }

    with YoutubeDL(options) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        video_id = info_dict.get("id", None)
        video_ext = info_dict.get("ext", None)
        video_title = info_dict.get("title", None)

        if not video_id:
            return None

        ydl.download([video_url])
        return (
            os.path.join(save_dir, f"{video_id}.{video_ext}"),
            video_id,
            video_title
        )
