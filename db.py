import sqlite3

class Database:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.__create_tables()

    def insert_yt_video_no_commit(
        self,
        yt_id: str,
        title: str
    ):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO yt_videos (yt_id, title) VALUES (?, ?)",
            (yt_id, title)
        )

    def insert_talk_no_commit(
        self,
        yt_id: str,
        start_sec: int,
        end_sec: int,
        comment: str
    ):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO talks (yt_id, start_sec, end_sec, comment) VALUES (?, ?, ?, ?)",
            (yt_id, start_sec, end_sec, comment)
        )

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

    def __create_tables(self):
        cursor = self.conn.cursor()

        # yt_videos テーブルが存在しなければ作成
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS yt_videos (
                yt_id VARCHAR(32) NOT NULL PRIMARY KEY,
                title VARCHAR(255) NOT NULL
            )
        """)

        # talks テーブルが存在しなければ作成
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS talks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                yt_id VARCHAR(32) NOT NULL,
                start_sec INTEGER NOT NULL,
                end_sec INTEGER NOT NULL,
                comment TEXT NOT NULL,
                FOREIGN KEY (yt_id) REFERENCES yt_videos(yt_id)
            )
        """)

        self.conn.commit()
