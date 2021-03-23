nclude <iostream>
#include <WinSock2.h>
#pragma comment (lib,"ws2_32.lib")
#include <thread>
char buf[4], coor[2];
char yeet;
char map[100];
int main() {
	map[45] = 1;
	WSADATA data;
	WORD ver = MAKEWORD(2, 2);
	WSAStartup(ver, &data);
	SOCKET sock = socket(AF_INET, SOCK_STREAM, 0);
	sockaddr_in adress;
	adress.sin_addr.S_un.S_addr = 0;
	adress.sin_port = htons(7778);
	adress.sin_family = AF_INET;
	bind(sock, (sockaddr*)&adress, sizeof(adress));
	listen(sock, SOMAXCONN);
	sockaddr client;
	int clientsize = sizeof(client);
	SOCKET clientsocket = accept(sock, &client, &clientsize);
	while (true) {
		recv(clientsocket, buf, 4, 0);
		std::cout << buf << std::endl;
	}
}
