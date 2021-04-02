#include "hoofd.h"
#include <SDL.h>
#include <fstream>
#include <iostream>
#include <windows.h>
#include <vector>
#include <random>
#include <chrono>
#pragma comment (lib,"ws2_32.lib")
SDL_Event even;
const int Gravity = 1;
const int player_size[3] = { 20,20,20};
const int player_polycount = 4;
float bullet_hitbox_var[7] = { 0,0,0,0,0,0,0};
int menu,shoot_delay = 0;
int mouseX[2], mouseY[2] = { 0,0 };
bool wait = 0;
float jump = 0;
float temp[2] = { 0,0 };
float playerloc[2] = { 20,20 };
float mov[2] = { 0,0 };
const int static_props = 5;

INPUT mscancel;
std::vector<std::vector<float>> pos;
int bullet_hitbox(std::vector<float> bullet[], std::vector<float> wall[]) {
	bullet_hitbox_var[0] = max(wall[0][1] , wall[0][3]) - min(wall[0][1], wall[0][3]);
	bullet_hitbox_var[1] = max(wall[0][2], wall[0][4]) - min(wall[0][2], wall[0][4]);
	bullet_hitbox_var[2] = bullet[0][3] - min(wall[0][1], wall[0][3]) + 50;
	bullet_hitbox_var[3] = bullet[0][4] - min(wall[0][2], wall[0][4]) + 50;
	bullet_hitbox_var[4] = (bullet_hitbox_var[0] / bullet_hitbox_var[2]);
	bullet_hitbox_var[5] = (bullet_hitbox_var[1] / bullet_hitbox_var[3]);
	if (bullet_hitbox_var[4] < bullet_hitbox_var[5]&&
		max(wall[0][1],wall[0][3]) > bullet[0][3] && min(wall[0][3], wall[0][1]) < bullet[0][3] && max(wall[0][2],wall[0][4]) > bullet[0][4] && min(wall[0][4],wall[0][2]) < bullet[0][2]) {
		bullet_hitbox_var[2] = bullet[0][3] - min(wall[0][1], wall[0][3]) - 50;
		bullet_hitbox_var[3] = bullet[0][4] - min(wall[0][2], wall[0][4]) - 50;
		bullet_hitbox_var[4] = (bullet_hitbox_var[0] / bullet_hitbox_var[2]);
		bullet_hitbox_var[5] = (bullet_hitbox_var[1] / bullet_hitbox_var[3]);
		if (bullet_hitbox_var[4] > bullet_hitbox_var[5]) {
			bullet_hitbox_var[2] = bullet[0][1] - min(wall[0][1], wall[0][3]) + 50;
			bullet_hitbox_var[3] = bullet[0][2] - min(wall[0][2], wall[0][4]) + 50;
			bullet_hitbox_var[4] = bullet_hitbox_var[0] / bullet_hitbox_var[2];
			bullet_hitbox_var[5] = bullet_hitbox_var[1] / bullet_hitbox_var[3];
			if (bullet_hitbox_var[4] < bullet_hitbox_var[5]) {
				bullet_hitbox_var[2] = bullet[0][1] - min(wall[0][1], wall[0][3]) - 50;
				bullet_hitbox_var[3] = bullet[0][2] - min(wall[0][2], wall[0][4]) - 50;
				bullet_hitbox_var[4] = bullet_hitbox_var[0] / bullet_hitbox_var[2];
				bullet_hitbox_var[5] = bullet_hitbox_var[1] / bullet_hitbox_var[3];
				if (bullet_hitbox_var[4] > bullet_hitbox_var[5]) {
					bullet_hitbox_var[0] = max(wall[0][1], wall[0][3]) / min(wall[0][1], wall[0][3]);
					bullet_hitbox_var[1] = max(wall[0][2], wall[0][4]) / min(wall[0][2], wall[0][4]);
					bullet_hitbox_var[2] = max(bullet_hitbox_var[0], bullet_hitbox_var[1]) / min(bullet_hitbox_var[0], bullet_hitbox_var[1]);
					bullet_hitbox_var[3] = bullet[0][3] - bullet[0][1];
					bullet_hitbox_var[4] = bullet[0][4] - bullet[0][2];
					bullet[0][4] = bullet[0][2];
					bullet[0][3] = bullet[0][1];
					while (abs(bullet[0][4] - bullet[0][2]) + abs(bullet[0][3] - bullet[0][1]) < 20) {
						bullet[0][3] -= bullet_hitbox_var[3] / 10;
						bullet[0][4] -= bullet_hitbox_var[4] / 10;
					}
				}
			}
		}
		
	}
	return 0;
}
int random(int x) {
	std::uniform_int_distribution<int> dist(0, x);
	int time = std::chrono::high_resolution_clock().now().time_since_epoch().count();
	std::default_random_engine rand(time);
	int randf = dist(rand);
	return randf;
}
int main(int argc, char* argv[]) {
	mscancel.type = INPUT_MOUSE;
	mscancel.mi.dwFlags = MOUSEEVENTF_MOVE;
	SDL_Window* window = SDL_CreateWindow("game", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 1000, 1000, NULL);
	SDL_Renderer* render = SDL_CreateRenderer(window, 0, NULL);
	SDL_GetMouseState(&mouseX[0], &mouseY[0]);
	init();
	float minXcoord = pos[0][1];
	float maxXcoord = pos[0][1];
	float minYcoord = pos[0][2];
	float maxYcoord = pos[0][2];
	while (true) {
		SDL_SetRenderDrawColor(render, 255, 0, 0, 255);
		for (int i = 0; i < pos.size(); i++) {
			if (pos[i][0] == 1) {
				SDL_SetRenderDrawColor(render, 255, pos[i][5], 0, 255);
			}
			SDL_RenderDrawLine(render, pos[i][1], pos[i][2], pos[i][3], pos[i][4]);
		}
		for (int i = 0; i < pos.size();) {
			switch ((int)pos[i][0]) {
			case 0:
				minXcoord = pos[0][1];
				maxXcoord = pos[0][1];
				minYcoord = pos[0][2];
				maxYcoord = pos[0][2];
				for (int i2 = i; i2 < i + player_polycount; i2++) {
					minXcoord = min(pos[i2][1], min(pos[i2][3], minXcoord));
					maxXcoord = max(pos[i2][1], max(pos[i2][3], maxXcoord));
					minYcoord = min(pos[i2][2], min(pos[i2][4], minYcoord));
					maxYcoord = max(pos[i2][2], max(pos[i2][4], maxYcoord));
				}
				//D
				if (GetKeyState(0x44) < 0) {
					mov[0] += 0.015;
				}
				//W
				if (GetKeyState(0x57) < 0) {
					mov[1] -= 0.015;
				}
				//A
				if (GetKeyState(0x41) < 0) {
					mov[0] -= 0.015;
				}
				//S
				if (GetKeyState(0x53) < 0) {
					mov[1] += 0.015;
				}
				if (GetKeyState(VK_SPACE) < 0) {
					if (maxXcoord - minXcoord <= 20 || maxYcoord - minYcoord <= 20) {
						jump = 4;
					}
				}
				if (GetKeyState(VK_LBUTTON) < 0) {
					if (shoot_delay == 0) {
						pos.push_back({ 1,pos[0][1],pos[0][2],pos[0][1] + ((pos[0][1] - minXcoord - 10)),pos[0][2] + ((pos[0][2] - minYcoord - 10 )),0 });
						shoot_delay = 0;
					}
				}
				for (int i2 = i; i2 < i + player_polycount; i2++){
					if (maxXcoord - minXcoord + maxYcoord - minYcoord > 40) {
						for (int i3 = 0; i3 < 100; i3++) {
							pos[i2][1] -= (pos[i2][1] - minXcoord - 10) / 10000;
							pos[i2][2] -= (pos[i2][2] - minYcoord - 10) / 10000;
							pos[i2][3] -= (pos[i2][3] - minXcoord - 10) / 10000;
							pos[i2][4] -= (pos[i2][4] - minYcoord - 10) / 10000;
							if (maxXcoord - minXcoord + maxYcoord - minYcoord < 40) {
								break;
							}
						}
					}
					if (jump > 0) {
						pos[i2][1] += (pos[i2][1] - minXcoord - 10) / (100 / jump);
						pos[i2][2] += (pos[i2][2] - minYcoord - 10) / (100 / jump);
						pos[i2][3] += (pos[i2][3] - minXcoord - 10) / (100 / jump);
						pos[i2][4] += (pos[i2][4] - minYcoord - 10) / (100 / jump);
					}
				}
				if (jump > 0) {
					jump -= 0.05;
				}
				SDL_GetMouseState(&mouseX[1],&mouseY[1]);
				if (mouseX[0] != mouseX[1] || mouseY[0] != mouseY[1]) {
					if (wait == 1) {
						wait = 0;
						goto overslaan;
					}
					for (int i2 = i; i2 < i + player_polycount; i2++) {
						for (int i3 = 0; i3 < 100; i3++) {
							pos[i2][1] -= ((pos[i2][2] - minYcoord - 10)) * (mouseX[0] - mouseX[1]) / 20000;
							pos[i2][2] += ((pos[i2][1] - minXcoord - 10)) * (mouseX[0] - mouseX[1]) / 20000;
							pos[i2][3] -= ((pos[i2][4] - minYcoord - 10)) * (mouseX[0] - mouseX[1]) / 20000;
							pos[i2][4] += ((pos[i2][3] - minXcoord - 10)) * (mouseX[0] - mouseX[1]) / 20000;
						}
					}
					mscancel.mi.dx = 250 - mouseX[1];
					mscancel.mi.dy = 250 - mouseY[1];
					wait = 1;
					SendInput(1, &mscancel, sizeof(mscancel));
				}
				overslaan:
				mouseX[0] = mouseX[1];
				mouseY[0] = mouseY[1]; 
				for (int i2 = i; i2 < i + player_polycount; i2++) {
					pos[i2][1] += mov[0];
					pos[i2][2] += mov[1];
					pos[i2][3] += mov[0];
					pos[i2][4] += mov[1];
				}
				movement();
				i += player_polycount;
				break;
			case 1:
				for (int i2 = 0; i2 < static_props; i2++) {
					switch ((int)pos[i2][0]) {
					case 2:
						if (bullet_hitbox(&pos[i], &pos[i2]) != 0) {
							bullet_hitbox(&pos[i], &pos[i2]);
						}
						break;
					}
				}
				temp[0] = pos[i][3] - pos[i][1];
				temp[1] = pos[i][4] - pos[i][2];
				pos[i][1] += temp[0] / 4;
				pos[i][2] += temp[1] / 4;
				pos[i][3] += temp[0] / 4;
				pos[i][4] += temp[1] / 4;
				pos[i][5] = 1;
				if (pos[i][5] == 255) {
					pos.erase(pos.begin() + i);
				}
				i += 1;
				break;
			case 2:
				i += 1;
				break;
			}
		}
		if (shoot_delay > 0) {
			shoot_delay -= 1;
		}
		std::cout << pos.size() << std::endl;
		SDL_RenderPresent(render);
		SDL_PollEvent(&even);
		SDL_SetRenderDrawColor(render, 0, 0, 0, 255);
		SDL_RenderClear(render);
			
	}
	return 0;
}
