import pyautogui
import keyboard
import time

def drag_with_alt_key():
    print("Press 'Alt' key to start dragging. Move the mouse to drag, release 'Alt' key to stop.")

    while True:
        # Altキーが押されたら左クリックを押した状態にして、ドラッグを開始
        if keyboard.is_pressed('alt'):  # Altキーの確認
            initial_x, initial_y = pyautogui.position()  # 初期マウス位置を取得
            print(f"Dragging started at ({initial_x}, {initial_y})")

            pyautogui.mouseDown(button='left')  # 左クリックを押した状態にする

            # Altキーが押されている間はドラッグを実行
            while keyboard.is_pressed('alt'):
                current_x, current_y = pyautogui.position()  # 現在のマウス位置を取得
                dx = current_x - initial_x
                dy = current_y - initial_y

                # ドラッグを実行
                if dx != 0 or dy != 0:
                    pyautogui.moveTo(current_x, current_y)  # マウスを現在位置に移動
                    initial_x, initial_y = current_x, current_y  # 初期位置を更新

                time.sleep(0.01)  # 過負荷を防ぐために少しスリープ

            # Altキーが離されたらドラッグを終了
            pyautogui.mouseUp(button='left')  # 左クリックを離す
            print("Dragging stopped.")

        # Escキーでスクリプトを終了
        if keyboard.is_pressed('esc'):
            print("Script terminated.")
            break

if __name__ == "__main__":
    drag_with_alt_key()
