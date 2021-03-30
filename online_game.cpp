#include <SDL.h>
#include <fstream>
#include <iostream>
#include <windows.h>
#include <WinSock2.h>
#include <vector>
#pragma comment (lib,"ws2_32.lib")
SDL_Event even;
const int Gravity = 3;
std::vector<int[4]> pos = {
	{30,20,40,40},
	{30,20,20,40},
	{40,40,20,40}
};
int main(int argc, char* argv[]) {
	SDL_INIT_EVERYTHING;
	SDL_Window *window = SDL_CreateWindow("game", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 500, 500, NULL);
	SDL_Renderer* render = SDL_CreateRenderer(window, 0, NULL);
	while (true) {
		SDL_SetRenderDrawColor(render, 255, 0, 0, 255);
		for (int i = 0; i < pos; i++) {
			if (pos4[i] > 400 || pos2[i] > 400) {
				goto main;
			}
		}
		for (int i = 0; i < sizeof(pos4) / 4; i++) {
			pos2[i] += Gravity;
			pos4[i] += Gravity;
		}
	main:
		for (int i = 0; i < sizeof(pos1) / 4; i++) {
			SDL_RenderDrawLine(render, pos1[i], pos2[i], pos3[i], pos4[i]);
		}
		if (GetKeyState(0x44) < 0) {
			for (int i = 0; i < 3; i++) {
				pos1[i] += 1;
				pos3[i] += 1;
			}
		}
		if (GetKeyState(0x57) < 0) {
			for (int i = 0; i < 3; i++) {
				pos2[i] -= 1;
				pos4[i] -= 1;
			}
		}
		if (GetKeyState(0x41) < 0) {
			for (int i = 0; i < 3; i++) {
				pos1[i] -= 1;
				pos3[i] -= 1;
			}
		}
		if (GetKeyState(0x53) < 0) {
			for (int i = 0; i < 3; i++) {
				pos2[i] += 1;
				pos4[i] += 1;
			}
		}
		if (GetKeyState(0x4E) < 0) {

		}
		SDL_RenderPresent(render);
		SDL_PollEvent(&even);
		SDL_SetRenderDrawColor(render, 0, 0, 0, 255);
		SDL_RenderClear(render);
		SDL_Delay(2);
	}
	return 0;
}
