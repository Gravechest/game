#include <iostream>
#include <WinSock2.h>
#pragma comment (lib,"ws2_32.lib")
#include <thread>
char buf[4];
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
			if (i % 10 == 0) {
				printf("\n");
			}
		}
		std::cin >> yeet;
		send(clientsocket, buf, yeet,0);
	}
}
