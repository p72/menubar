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
            "Chrome",
            "Safari", 
            "ChatGPT",
            "Finder",
            "Obsidian",
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
    
    def switch_to_app(self, app_name, bundle_id=None):
        """アプリに切り替える（起動中の場合のみ）"""
        try:
            if bundle_id:
                # バンドルIDでアプリをアクティブにする
                result = subprocess.run(
                    ["osascript", "-e", f'tell application "System Events" to set frontmost of process "{app_name}" to true'],
                    capture_output=True,
                    text=True
                )
            else:
                # アプリ名でアクティブにする
                result = subprocess.run(
                    ["osascript", "-e", f'tell application "{app_name}" to activate'],
                    capture_output=True,
                    text=True
                )
            
            # エラーが発生した場合（アプリが起動していない）
            if result.returncode != 0:
                rumps.notification(
                    title=f"{app_name}",
                    subtitle="Not Running",
                    message=f"{app_name} is not currently running"
                )
            else:
                rumps.notification(
                    title=f"{app_name}",
                    subtitle="Switched",
                    message=f"Switched to {app_name}"
                )
                
        except Exception as e:
            rumps.notification(
                title=f"{app_name}",
                subtitle="Error",
                message=f"Could not switch to {app_name}"
            )
    
    @rumps.clicked("Chrome")
    def switch_to_chrome(self, _):
        """Chromeに切り替え"""
        self.switch_to_app("Google Chrome")
    
    @rumps.clicked("Safari")
    def switch_to_safari(self, _):
        """Safariに切り替え"""
        self.switch_to_app("Safari")
    
    @rumps.clicked("ChatGPT")
    def switch_to_chatgpt(self, _):
        """ChatGPTに切り替え"""
        self.switch_to_app("ChatGPT")
    
    @rumps.clicked("Finder")
    def switch_to_finder(self, _):
        """Finderに切り替え"""
        self.switch_to_app("Finder")
    
    @rumps.clicked("Obsidian")
    def switch_to_obsidian(self, _):
        """Obsidianに切り替え"""
        self.switch_to_app("Obsidian")
    
    @rumps.clicked("Quit")
    def quit_app(self, _):
        """アプリを終了"""
        rumps.quit_application()

if __name__ == "__main__":
    app = MissionControlApp()
    app.run() 