import pygame
import sys

# 定数
WINDOWED_SIZE = (1280, 720)
FULLSCREEN_SIZE = (0, 0)  # 0,0でフルスクリーンモード

# ゲーム終了処理
def exit_game():
  pygame.quit()
  sys.exit()

# 画面サイズ切り替え
def change_display_size(screen, is_fullscreen):
  new_mode = FULLSCREEN_SIZE if not is_fullscreen else WINDOWED_SIZE
  screen = pygame.display.set_mode(new_mode, pygame.FULLSCREEN if not is_fullscreen else 0)
  return screen, not is_fullscreen

# イベント処理
def handle_event(event, screen, is_fullscreen):
  if event.type == pygame.QUIT:
    exit_game()
  elif event.type == pygame.KEYDOWN:
    # Alt + Enterでフルスクリーンとウィンドウモードを切り替え
    if event.key == pygame.K_RETURN and pygame.key.get_mods() & pygame.KMOD_ALT:
      screen, is_fullscreen = change_display_size(screen, is_fullscreen)
    # ESCでゲーム終了
    elif event.key == pygame.K_ESCAPE:
      exit_game()
  return screen, is_fullscreen

# メイン関数
def main():
  pygame.init()
  screen = pygame.display.set_mode(WINDOWED_SIZE)
  pygame.display.set_caption("trade_simulation_game")

  # フルスクリーンのフラグ
  is_fullscreen = False

  # メインループ
  while True:
    for event in pygame.event.get():
      screen, is_fullscreen = handle_event(event, screen, is_fullscreen)

    # 画面を白で塗りつぶす
    screen.fill((255, 255, 255))

    # 画面を更新
    pygame.display.flip()

# 実行
if __name__ == "__main__":
  main()
