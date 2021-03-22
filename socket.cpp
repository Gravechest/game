#include <iostream>
#include <WinSock2.h>
#pragma comment (lib,"ws2_32.lib")
#include <thread>
char buf[8],coor[2];
char yeet;
char map[100];
void search() {

}
int main() {
	map[45] = 1;
	WSADATA data;
	WORD ver = MAKEWORD(2, 2);
	WSAStartup(ver, &data);
	SOCKET sock = socket(AF_INET, SOCK_STREAM, 0);
	sockaddr_in adress;
	adress.sin_addr.S_un.S_addr = INADDR_ANY;
	adress.sin_port = htons(7778);
	adress.sin_family = AF_INET;
	bind(sock, (sockaddr*)&adress, sizeof(adress));
	listen(sock, SOMAXCONN);
	sockaddr client;
	int clientsize = sizeof(client);
	SOCKET clientsocket = accept(sock, &client,&clientsize);
	while (true) {
		for (int i = 0; i < 100; i++) {
			switch (map[i]) {
			case 0:
				printf(".");
				break;
			case 1:
				printf("1");
				break;
			case 2:
				printf("2");
				break;
			}
			if (i % 10 == 9) {
				printf("\n");
			}
		}
		printf("\x1b[H");
		for (int i = 0;i < 2;){
			recv(clientsocket, buf, 8, 0);
			if (buf[0] != 0) {
				coor[i] = buf[0] - 49;
				i++;
			}
		}
		map[coor[0] + coor[1] * 10] = 2;
		std::cout << "yeet";
	}
}
