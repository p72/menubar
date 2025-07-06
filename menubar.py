#!/usr/bin/env python3
import rumps
import subprocess
import os

# 環境変数の変更を完全に削除した正式版
# CursorのPython環境に影響しないMission Controlアプリ

class MissionControlApp(rumps.App):
    def __init__(self):
        super().__init__("🚀", quit_button=None)
        self.menu = [
            "Mission Control", 
            None,  # 罫線（セパレーター）
            "Quit"
        ]
    
    @rumps.clicked("Mission Control")
    def open_mission_control(self, _):
        """メニューバーアイコンをクリックしたときにMission Controlを起動"""
        try:
            # Mission Controlアプリを直接起動（権限不要）
            subprocess.run(["open", "-a", "Mission Control"], check=True)
            
        except subprocess.CalledProcessError:
            # エラーが発生した場合は、代替方法を試す
            try:
                # Exposé/Mission Controlを起動
                subprocess.run(["open", "-b", "com.apple.expose.front.no-mouse"], check=True)
                
            except subprocess.CalledProcessError:
                # それでも失敗した場合はエラー通知
                rumps.notification(
                    title="Mission Control",
                    subtitle="Failed!",
                    message="Could not launch Mission Control"
                )
    

    
    @rumps.clicked("Quit")
    def quit_app(self, _):
        """アプリを終了"""
        rumps.quit_application()

if __name__ == "__main__":
    app = MissionControlApp()
    app.run() 