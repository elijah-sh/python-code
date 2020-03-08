import pygame, sys, random
# different images for the skier depending on his direction
skier_images = ["D:/tmp/data/image/skier_down.png", "D:/tmp/data/image/skier_right1.png", "D:/tmp/data/image/skier_right2.png", "D:/tmp/data/image/skier_left2.png", "D:/tmp/data/image/skier_left1.png"]

# 创建滑雪者
# class for the Skier sprite
class SkierClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("D:/tmp/data/image/skier_down.png")
        self.rect = self.image.get_rect()
        self.rect.center = [320, 100]
        self.angle = 0