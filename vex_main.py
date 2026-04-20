
import sys
import vlc
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QFileDialog, QSlider
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QIcon

class VexPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VEX PLAYER - Ultimate Vision")
        self.resize(1000, 700)
        
        # UI Styling (VEX Dark Mode)
        self.setStyleSheet("background-color: #0f3460; color: white;")

        # --- VLC Engine Setup ---
        self.instance = vlc.Instance()
        self.media_player = self.instance.media_player_new()

        # --- Main Layout ---
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Video Frame (Eneo ambalo picha itatokea)
        self.video_frame = QWidget()
        self.video_frame.setStyleSheet("background-color: black; border: 2px solid #e94560; border-radius: 10px;")
        self.layout.addWidget(self.video_frame)

        # Seek Bar (Slider ya kusogeza video mbele/nyuma)
        self.seek_bar = QSlider(Qt.Orientation.Horizontal)
        self.layout.addWidget(self.seek_bar)

        # --- Buttons Area ---
        self.controls = QHBoxLayout()
        
        self.open_btn = QPushButton("OPEN MOVIE")
        self.play_btn = QPushButton("PLAY/PAUSE")
        
        # Style ya Buttons
        btn_style = "background-color: #e94560; color: white; padding: 12px; font-weight: bold; border-radius: 8px;"
        self.open_btn.setStyleSheet(btn_style)
        self.play_btn.setStyleSheet(btn_style)

        self.controls.addWidget(self.open_btn)
        self.controls.addWidget(self.play_btn)
        self.layout.addLayout(self.controls)

        # Logic za Button
        self.open_btn.clicked.connect(self.open_file)
        self.play_btn.clicked.connect(self.play_pause)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Chagua Movie", "", "Video Files (*.mp4 *.mkv *.avi *.ts)")
        if file_path:
            media = self.instance.media_new(file_path)
            self.media_player.set_media(media)
            
            # Kitaalam: Unganisha VLC na Window ya PyQt
            if sys.platform == "win32":
                self.media_player.set_hwnd(int(self.video_frame.winId()))
            
            self.media_player.play()

    def play_pause(self):
        if self.media_player.is_playing():
            self.media_player.pause()
        else:
            self.media_player.play()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = VexPlayer()
    # Kwenye Colab tunasave tu, haitafungua window mpaka tuigeuze kuwa .exe
    print("✅ VEX PLAYER Engine integrated successfully in vex_main.py")
