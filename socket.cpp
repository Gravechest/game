#include <iostream>
#include <WinSock2.h>
#pragma comment (lib,"ws2_32.lib")
#include <thread>
char yeet;
char map[100];
char msg;
int main() {
	map[45] = 1;
	WSADATA data;
	WORD ver = MAKEWORD(2, 2);
	WSAStartup(ver, &data);
	SOCKET sock = socket(AF_INET, SOCK_STREAM, 0);
	sockaddr_in adres;
	adres.sin_addr.S_un.S_addr = 167946432;
	adres.sin_port = htons(7778);
	adres.sin_family = AF_INET;
	connect(sock, (sockaddr*)&adres, sizeof(adres));
	while (true) {
		std::cin >> msg;
		std::cout << &msg;
		send(sock, &msg, 2, 0);
	}
}
