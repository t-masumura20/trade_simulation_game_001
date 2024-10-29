import pygame
import sys

# 定数
WINDOWED_SIZE = (1280, 720)
FULLSCREEN_SIZE = (0, 0)  # 0,0でフルスクリーンモード

# ゲーム管理クラス
class Game:
  def __init__(self):
    # 初期化
    pygame.init()
    self.is_fullscreen = False
    self.screen = pygame.display.set_mode(WINDOWED_SIZE)
    pygame.display.set_caption("trade_simulation_game")
    
    # 背景画像の読み込みとスケーリング
    self.background_image = pygame.image.load("images/city_001.png")
    self.update_background()

  # 背景画像のスケーリング
  def update_background(self):
    screen_size = self.screen.get_size()
    self.scaled_background = pygame.transform.scale(self.background_image, screen_size)

  # 画面サイズ切り替え
  def toggle_fullscreen(self):
    new_mode = FULLSCREEN_SIZE if not self.is_fullscreen else WINDOWED_SIZE
    self.screen = pygame.display.set_mode(new_mode, pygame.FULLSCREEN if not self.is_fullscreen else 0)
    self.is_fullscreen = not self.is_fullscreen
    self.update_background()  # 画面サイズ変更後に背景画像を再スケーリング

  # イベント処理
  def handle_event(self, event):
    if event.type == pygame.QUIT:
      self.exit_game()
    elif event.type == pygame.KEYDOWN:
      # Alt + Enterでフルスクリーンとウィンドウモードを切り替え
      if event.key == pygame.K_RETURN and pygame.key.get_mods() & pygame.KMOD_ALT:
        self.toggle_fullscreen()
      # Escキーでゲーム終了
      elif event.key == pygame.K_ESCAPE:
        self.exit_game()

  # ゲーム終了処理
  def exit_game(self):
    pygame.quit()
    sys.exit()

  # メインループ
  def run(self):
    while True:
      for event in pygame.event.get():
        self.handle_event(event)

      # 背景画像の描画
      self.screen.blit(self.scaled_background, (0, 0))

      # 画面を更新
      pygame.display.flip()

# 実行
if __name__ == "__main__":
  game = Game()
  game.run()