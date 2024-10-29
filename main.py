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
def change_display_size(screen, is_fullscreen, background_image):
  new_mode = FULLSCREEN_SIZE if not is_fullscreen else WINDOWED_SIZE
  screen = pygame.display.set_mode(new_mode, pygame.FULLSCREEN if not is_fullscreen else 0)

  # 背景画像を画面サイズに合わせてスケーリング
  screen_size = screen.get_size()
  scaled_background = pygame.transform.scale(background_image, screen_size)

  return screen, not is_fullscreen, scaled_background

# イベント処理
def handle_event(event, screen, is_fullscreen, background_image):
  if event.type == pygame.QUIT:
    exit_game()
  elif event.type == pygame.KEYDOWN:
    # Alt + Enterでフルスクリーンとウィンドウモードを切り替え
    if event.key == pygame.K_RETURN and pygame.key.get_mods() & pygame.KMOD_ALT:
      screen, is_fullscreen, background_image = change_display_size(screen, is_fullscreen, background_image)
    # ESCでゲーム終了
    elif event.key == pygame.K_ESCAPE:
      exit_game()
  return screen, is_fullscreen, background_image

# メイン関数
def main():
  pygame.init()
  screen = pygame.display.set_mode(WINDOWED_SIZE)
  pygame.display.set_caption("trade_simulation_game")

  # フルスクリーンのフラグ
  is_fullscreen = False

  # 背景画像の読み込み
  background_image = pygame.image.load("images/city_001.png")
  background_image = pygame.transform.scale(background_image, WINDOWED_SIZE)

  # メインループ
  while True:
    for event in pygame.event.get():
      screen, is_fullscreen, background_image = handle_event(event, screen, is_fullscreen, background_image)

    # 背景画像の描画
    screen.blit(background_image, (0, 0))

    # 画面を更新
    pygame.display.flip()

# 実行
if __name__ == "__main__":
  main()
