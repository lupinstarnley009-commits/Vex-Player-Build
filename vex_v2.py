
import sys
import requests
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QPushButton, QHBoxLayout, QFileDialog, QSlider, QLabel, QMessageBox)
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import Qt, QUrl, QTimer

VERSION = "2.0.0"
UPDATE_URL = "https://raw.githubusercontent.com/lupinstarnley009-commits/Vex-Player-Build/main/version.txt"

class VexPlayerV2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"VEX PLAYER V2 - {VERSION}")
        self.resize(1000, 700)
        self.setStyleSheet("background-color: #0f172a; color: #f8fafc;")

        # --- Multimedia Engine ---
        self.media_player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.media_player.setAudioOutput(self.audio_output)

        # --- UI Layout ---
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Video Screen (Glassmorphism effect placeholder)
        self.video_widget = QVideoWidget()
        self.video_widget.setStyleSheet("background-color: #000; border: 1px solid #334155; border-radius: 12px;")
        self.layout.addWidget(self.video_widget)
        self.media_player.setVideoOutput(self.video_widget)

        # Controls
        self.controls = QHBoxLayout()
        self.open_btn = QPushButton("📂 OPEN")
        self.play_btn = QPushButton("▶ PLAY")
        
        for btn in [self.open_btn, self.play_btn]:
            btn.setStyleSheet("background-color: #3b82f6; color: white; padding: 10px; border-radius: 8px; font-weight: bold;")
        
        self.controls.addWidget(self.open_btn)
        self.controls.addWidget(self.play_btn)
        self.layout.addLayout(self.controls)

        # Connections
        self.open_btn.clicked.connect(self.open_file)
        self.play_btn.clicked.connect(self.play_pause)

        # Auto-Update Check (Itafanya kazi kukiwa na internet)
        QTimer.singleShot(3000, self.check_updates)

    def open_file(self):
        file_dialog = QFileDialog()
        file_url, _ = file_dialog.getOpenFileUrl(self, "Chagua Video", QUrl(), "Videos (*.mp4 *.mkv *.avi)")
        if file_url:
            self.media_player.setSource(file_url)
            self.media_player.play()

    def play_pause(self):
        if self.media_player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.media_player.pause()
        else:
            self.media_player.play()

    def check_updates(self):
        try:
            response = requests.get(UPDATE_URL, timeout=5)
            cloud_version = response.text.strip()
            if cloud_version > VERSION:
                QMessageBox.information(self, "Update Inapatikana", f"VEX Version mpya ({cloud_version}) ipo tayari!")
        except:
            pass # Offline mode - hakuna shida

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = VexPlayerV2()
    player.show()
    sys.exit(app.exec())
