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
            "Cursor",
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
                # エラーは静かに無視（通知を使わない）
                pass
    
    def switch_to_app(self, app_name):
        """アプリに切り替える（起動中の場合のみ）"""
        try:
            # AppleScriptでアプリをアクティブにする
            script = f'''
            tell application "System Events"
                set appProcess to first process whose name is "{app_name}"
                set frontmost of appProcess to true
            end tell
            '''
            
            result = subprocess.run(
                ["osascript", "-e", script],
                capture_output=True,
                text=True
            )
            
            # エラーが発生した場合（アプリが起動していない）は静かに無視
            # 成功した場合は何もしない（静かに切り替わる）
            
        except Exception:
            # エラーは静かに無視
            pass
    
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
    
    @rumps.clicked("Cursor")
    def switch_to_cursor(self, _):
        """Cursorに切り替え"""
        self.switch_to_app("Cursor")
    
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