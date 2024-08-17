import pyautogui
import keyboard
import pygetwindow as gw
import threading
import argparse

def move_active_window(modifier_key):
    active_window = gw.getActiveWindow()  # 現在アクティブなウィンドウを取得

    if active_window:
        initial_x, initial_y = pyautogui.position()  # 修飾キーを押した時のカーソル位置を取得
        initial_window_x, initial_window_y = active_window.left, active_window.top

        while keyboard.is_pressed(modifier_key) and not keyboard.is_pressed('shift'):
            current_x, current_y = pyautogui.position()  # 現在のカーソル位置を取得
            dx = current_x - initial_x
            dy = current_y - initial_y

            # ウィンドウの位置を更新
            active_window.moveTo(initial_window_x + dx, initial_window_y + dy)

def resize_active_window(modifier_key):
    active_window = gw.getActiveWindow()  # 現在アクティブなウィンドウを取得

    if active_window:
        initial_x, initial_y = pyautogui.position()  # 修飾キー＋Shiftキーを押した時のカーソル位置を取得
        initial_width, initial_height = active_window.width, active_window.height

        while keyboard.is_pressed(modifier_key) and keyboard.is_pressed('shift'):
            current_x, current_y = pyautogui.position()  # 現在のカーソル位置を取得
            dx = current_x - initial_x
            dy = current_y - initial_y

            # ウィンドウのサイズを更新
            new_width = max(100, initial_width + dx)  # 最小幅100ピクセルに制限
            new_height = max(100, initial_height + dy)  # 最小高さ100ピクセルに制限

            active_window.resizeTo(new_width, new_height)

def block_context_menu():
    # Context Menuキーのデフォルトの動作をブロックする
    keyboard.block_key('menu')

def check_keys(stop_event, modifier_key):
    while not stop_event.is_set():
        if keyboard.is_pressed(modifier_key) and not keyboard.is_pressed('shift'):
            move_active_window(modifier_key)
        elif keyboard.is_pressed(modifier_key) and keyboard.is_pressed('shift'):
            resize_active_window(modifier_key)

# コマンドライン引数を処理
parser = argparse.ArgumentParser(description='Choose the modifier key to move or resize windows.')
parser.add_argument('--key', choices=['alt', 'context'], default='context',
                    help='Choose the modifier key: "alt" for Alt key, "context" for Context Menu key (default).')
args = parser.parse_args()

# 選択された修飾キー
modifier_key = 'alt' if args.key == 'alt' else 'menu'

# Context Menuキーが修飾キーとして選択された場合、その本来の機能をブロック
if modifier_key == 'menu':
    block_context_menu()

# 終了のためのスレッド停止イベント
stop_event = threading.Event()

# キー状態を監視するスレッドを開始
thread = threading.Thread(target=check_keys, args=(stop_event, modifier_key))
thread.start()

try:
    keyboard.wait('esc')  # Escキーを押すまで待機
finally:
    stop_event.set()  # スレッドを停止させる
    thread.join()     # スレッドの終了を待つ
    print("スクリプトを終了しました。")
