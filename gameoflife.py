
import pygame
from random import *
import numpy as np
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("type",help = "editor or random")
args = parser.parse_args()
width = 1000
height = 1000
resolution = 10
row = width//resolution
col = height//resolution
def create_world(row,col):
	world = np.zeros((int(row),int(col)),dtype = int)
	return world
def setup(grid):
	for i in range(row):
		for j in range(col):
			grid[i][j] = randrange(0,2)
def count_neighbours(grid,x,y):
  s = 0;
  for i in range(-1,2):
    for j in range(-1,2):
    	s += grid[(x + i + col) % col][(y + j + row) % row]
  s -= grid[x][y];
  return s;
def editor():
	pygame.init()
	window = pygame.display.set_mode((width,height))
	fps = pygame.time.Clock()
	global grid
	while(1):
		verify = 1
		while(1 and verify):
			window.fill(pygame.Color(255,255,255))
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_s:
						verify = 0
					if event.key == pygame.K_r:
						for i in range(col):
							for j in range(row):
								grid[i][j] = 0
				elif event.type == pygame.MOUSEBUTTONDOWN:
					y,x = event.pos
					y //= resolution
					x //= resolution
					grid[y][x] = 1 if not grid[y][x] else 0
				elif event.type == pygame.MOUSEMOTION:
					y,x = event.pos
					y //= resolution
					x //= resolution
					if pygame.mouse.get_pressed()[0]:
						grid[y][x] = 1
					if pygame.mouse.get_pressed()[2]:
						grid[y][x] = 0			
			for i in range(col):
				for j in range(row):
					x = i*resolution
					y = j*resolution
					if grid[i][j]:
						rect = pygame.Rect(x, y, resolution-1, resolution-1)
						pygame.draw.rect(window, (0,0,0), rect)
			pygame.event.pump()
			pygame.display.flip()
		verify = 1
		while(1 and verify):
			window.fill(pygame.Color(255,255,255))
			for event in pygame.event.get():
				if event.type==pygame.KEYDOWN:
					if event.key == pygame.K_q:
						pygame.quit()
						sys.exit()
					if event.key == pygame.K_p:
						verify = 0
				elif event.type == pygame.MOUSEMOTION:
					y,x = event.pos
					y //= resolution
					x //= resolution
					if pygame.mouse.get_pressed()[0]:
						grid[y][x] = 1
					if pygame.mouse.get_pressed()[2]:
						grid[y][x] = 0
			for i in range(col):
				for j in range(row):
					x = i*resolution
					y = j*resolution
					if grid[i][j]:
						rect = pygame.Rect(x, y, resolution-1, resolution-1)
						pygame.draw.rect(window, (0,0,0), rect)
			new = create_world(col,row)
			for i in range(col):
				for j in range(row):
					state = grid[i][j]
					count = count_neighbours(grid,i,j)
					if state == 0 and count == 3 :
						new[i][j] = 1;
					elif state  and (count < 2 or count > 3):
						new[i][j] = 0;
					else :
						new[i][j] = state;
			grid = new
			pygame.event.pump()
			pygame.display.flip()
			
def random_mode():
	pygame.init()
	window = pygame.display.set_mode((width,height))
	fps = pygame.time.Clock()
	global grid
	setup(grid)
	while(1):
		window.fill(pygame.Color(0,0,0))
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key == pygame.K_p:
					pygame.quit()
					sys.exit()
		for i in range(col):
			for j in range(row):
				x = i*resolution
				y = j*resolution
				if grid[i][j]:
					rect = pygame.Rect(x, y, resolution-1, resolution-1)
					pygame.draw.rect(window, (225,225,225), rect)
		new = create_world(col,row)
		for i in range(col):
			for j in range(row):
				state = grid[i][j]
				count = count_neighbours(grid,i,j)
				if state == 0 and count == 3 :
					new[i][j] = 1;
				elif state  and (count < 2 or count > 3):
					new[i][j] = 0;
				else :
					new[i][j] = state;
		grid = new
		pygame.display.flip()
grid = create_world(row,col)

if args.type == "editor":
	editor()
elif args.type == "random":
	random_mode()
















