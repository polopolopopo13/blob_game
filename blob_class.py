import random
import pygame
import numpy as np
import time

class PnjBlob():
	def __init__(self, color, x_boundary, y_boundary):
		self.size = random.randrange(4, 8)
		self.color = color
		self.x_boundary = x_boundary
		self.y_boundary = y_boundary
		self.x = random.randrange(0, self.x_boundary)
		self.y = random.randrange(0, self.y_boundary)
		self.move_x = random.randrange(-4, 4)
		self.move_y = random.randrange(-4, 4)
		self.speed = 1

	def move(self):
		self.x += int(self.move_x * self.speed)
		self.y += int(self.move_y * self.speed)

	def check_boundaries(self):
		if self.x < 0: self.x = self.x_boundary
		elif self.x > self.x_boundary: self.x = 0

		if self.y < 0: self.y = self.y_boundary
		elif self.y > self.y_boundary: self.y = 0

#class VoidHole():
class VoidHole(PnjBlob):
	def __init__(self, color, x_boundary, y_boundary):
		self.size = 11
		self.color = color
		self.x_boundary = x_boundary
		self.y_boundary = y_boundary
		self.x = random.randrange(0, self.x_boundary)
		self.y = random.randrange(0, self.y_boundary)
		self.move_x = random.randrange(-2, 2)
		self.move_y = random.randrange(-2, 2)
		self.speed = 1

	def creating(self, x_boundary, y_boundary):
		self.size *= 0.95
		_whithy = PnjBlob((255,255,255), x_boundary, y_boundary)
		_whithy.size = 3
		_whithy.x = self.x
		_whithy.y = self.y
		return _whithy

	def absorbing(self):
		self.size *= 1.1

class UserBlob():
	def __init__(self, color, x_boundary, y_boundary, is_alive):
		self.size = 8
		self.alive = is_alive
		self.color = color
		self.x_boundary = x_boundary
		self.y_boundary = y_boundary
		self.x = random.randrange(0, self.x_boundary)
		self.y = random.randrange(0, self.y_boundary)
		self.power = dict()

	def user_move(self, direction):
		if direction == 'move_left':
			self.x -= 5
		if direction == 'move_right':
			self.x += 5
		if direction == 'move_down':
			self.y += 5
		if direction == 'move_up':
			self.y -= 5

	def check_boundaries(self):
		if self.x < 0: self.x = self.x_boundary
		elif self.x > self.x_boundary: self.x = 0

		if self.y < 0: self.y = self.y_boundary
		elif self.y > self.y_boundary: self.y = 0



class InBox():
	def __init__(self, x, y , w, h, color, text):
		self.x = None
		self.y = None
		self.w = None
		self.h = None
		self.color = None
		self.text = None
'''
	def handle_mouse(self, event):
		if event.type == pygame.MOUSEBUTTOMLEFT:

'''