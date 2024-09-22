import pyautogui
import keyboard
import pygetwindow as gw
import threading
import time

# Contextキーの機能を無効化
keyboard.block_key('menu')

def move_active_window():
    active_window = gw.getActiveWindow()  # 現在アクティブなウィンドウを取得
    if active_window:
        initial_x, initial_y = pyautogui.position()  # Shiftキーを押した時のカーソル位置を取得
        initial_window_x, initial_window_y = active_window.left, active_window.top

        while keyboard.is_pressed('shift') and not keyboard.is_pressed('menu'):
            current_x, current_y = pyautogui.position()  # 現在のカーソル位置を取得
            dx = current_x - initial_x
            dy = current_y - initial_y

            # マウスが動いた時だけウィンドウを更新
            if dx != 0 or dy != 0:
                new_window_x = initial_window_x + dx
                new_window_y = initial_window_y + dy
                active_window.moveTo(new_window_x, new_window_y)
                initial_x, initial_y = current_x, current_y
                initial_window_x, initial_window_y = new_window_x, new_window_y

            time.sleep(0.1)  # スリープ時間を少し長くしてCPU負荷を軽減

def resize_active_window():
    active_window = gw.getActiveWindow()  # 現在アクティブなウィンドウを取得
    if active_window:
        initial_x, initial_y = pyautogui.position()  # Shiftキー＋Contextキーを押した時のカーソル位置を取得
        initial_width, initial_height = active_window.width, active_window.height

        while keyboard.is_pressed('shift') and keyboard.is_pressed('menu'):
            current_x, current_y = pyautogui.position()  # 現在のカーソル位置を取得
            dx = current_x - initial_x
            dy = current_y - initial_y

            # マウスが動いた時だけウィンドウのサイズを更新
            if dx != 0 or dy != 0:
                new_width = max(100, initial_width + dx)  # 最小幅100ピクセルに制限
                new_height = max(100, initial_height + dy)  # 最小高さ100ピクセルに制限
                active_window.resizeTo(new_width, new_height)

            time.sleep(0.1)  # スリープ時間を調整してCPU負荷を軽減

def drag_with_context_key():
    # Context Menuキーが押されたらドラッグ操作を開始
    if keyboard.is_pressed('menu'):
        initial_x, initial_y = pyautogui.position()  # 初期マウス位置を取得

        pyautogui.mouseDown(button='left')  # 左クリックを押した状態にする

        while keyboard.is_pressed('menu'):
            current_x, current_y = pyautogui.position()  # 現在のマウス位置を取得
            dx = current_x - initial_x
            dy = current_y - initial_y

            if dx != 0 or dy != 0:
                pyautogui.moveTo(current_x, current_y)  # マウスを移動
                initial_x, initial_y = current_x, current_y  # 新しい初期位置を更新

            time.sleep(0.05)  # スリープ時間を少し長く設定

        pyautogui.mouseUp(button='left')  # 左クリックを離す

def check_keys(stop_event):
    while not stop_event.is_set():
        if keyboard.is_pressed('shift') and not keyboard.is_pressed('menu'):
            move_active_window()  # Shiftキーのみでウィンドウ移動
        elif keyboard.is_pressed('shift') and keyboard.is_pressed('menu'):
            resize_active_window()  # Shiftキー+Contextキーでウィンドウリサイズ
        elif keyboard.is_pressed('menu'):
            drag_with_context_key()  # Contextキーでドラッグ操作
        time.sleep(0.05)  # メインループに少しスリープを追加して負荷軽減

# 終了のためのスレッド停止イベント
stop_event = threading.Event()

# キー状態を監視するスレッドを開始
thread = threading.Thread(target=check_keys, args=(stop_event,))
thread.start()

try:
    # スクリプトの動作を継続し、手動終了するまで待機
    while True:
        time.sleep(1)  # 無限ループで1秒ごとに処理を継続
finally:
    stop_event.set()  # スレッドを停止させる
    thread.join()     # スレッドの終了を待つ
