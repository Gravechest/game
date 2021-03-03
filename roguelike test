#include "libtcod.hpp"
#include <random>
#include <iostream>
#include <vector>
#include <chrono>
std::vector<std::vector<int>> mapgen;
std::vector<std::vector<int>> rays;
int player;
int itt = 0;
int itt2 = 0;
bool check = 0;
bool check2 = 0;
void comp(int x,int y) {
    for (int i = 0; i < mapgen.size(); i++) {
        if (mapgen[i][1] == x && mapgen[i][2] == y) {
            check = 1;
            return;
        }
    }
    check = 0;
}
std::pair<int,int>randcoor(int x , int y) {
    int time = std::chrono::high_resolution_clock().now().time_since_epoch().count() * 100;
    int time2 = std::chrono::high_resolution_clock().now().time_since_epoch().count() * 200;
    std::default_random_engine rand(time);
    std::default_random_engine rand2(time2);
    return{ time % x, time2 % y };
}
int rand(int x) {
    int time = std::chrono::high_resolution_clock().now().time_since_epoch().count() * 100;
    std::default_random_engine rand(time);
    return(time % x);
}
void gen(int x,int y,int type,int r,int g,int b) {
    mapgen.push_back(std::vector<int>());
    mapgen[itt].push_back(type);
    mapgen[itt].push_back(y);
    mapgen[itt].push_back(x);
    mapgen[itt].push_back(r);
    mapgen[itt].push_back(g);
    mapgen[itt].push_back(b);
    itt += 1;
}
void hitbox(int y,int x) {
    for (int i = 0; i < mapgen.size(); i++) {
        if (mapgen[i][1] == mapgen[player][1] + y && mapgen[i][2] == mapgen[player][2] + x) {
            return;
        };
    }
    mapgen[player][1] += y;
    mapgen[player][2] += x;
    check2 = 1;
}
int main() {
    int n = 0;
    std::uniform_int_distribution<int> dist(0, 2000);
    TCODConsole::initRoot(100, 50, "Gravechest", false);
    TCODConsole::root->setCustomFont("D:/rommelhoekje/tekenen/lekker tekenen/Debug/font/terminal16x16_gs_ro.png");
    TCODConsole::root->setFullscreen(0);
    for (int i = n; i < n + 5000; i++) {
        std::default_random_engine rand(i);
        if (dist(rand) == 0) {
            gen(i / 100, i % 100, 50, 255, 255, 255);
        }
    }

    if (check == 0) {
        player = itt;
        gen(0, 0, 4, 255, 0, 0);
    }
    check = 0;
    while (!TCODConsole::isWindowClosed()) {
        TCODConsole::root->clear();
        //mapgen
        for (int i = 0; i < mapgen.size(); i++) {
            check = 0;
            int xcoor = mapgen[i][2] - mapgen[player][2];
            int ycoor = mapgen[i][1] - mapgen[player][1];
            int absxcoor = abs(xcoor);
            int absycoor = abs(ycoor);
            float maxcoor = std::max(absxcoor, absycoor);
            float mincoor = std::min(absxcoor, absycoor);
            float sub = mincoor / maxcoor;
            for (int i2 = maxcoor; i2 >= 0; i2--) {
                int mincoorf = std::round(mincoor);
                if (absxcoor > absycoor) {
                    if (ycoor < 0) {
                        mincoorf = 0 - mincoorf;
                    }
                    if (xcoor < 0) {
                        i2 = 0 - i2;
                    }
                    TCODConsole::root->setCharBackground(mincoorf + mapgen[player][1], i2 + mapgen[player][2], {55,55,0});
                    if (TCODConsole::root->getChar(mincoorf + mapgen[player][1], i2 + mapgen[player][2]) == 50) {
                        check = 1;
                        break;
                    }
                    if (xcoor < 0) {
                        i2 = 0 - i2;
                    }
                    if (ycoor < 0) {
                        mincoorf = 0 - mincoorf;
                    }
                }
                else {
                    if (xcoor <= 0) {
                        mincoorf = 0 - mincoorf;
                    }
                    if (ycoor < 0) {
                        i2 = 0 - i2;    
                    }
                    TCODConsole::root->setCharBackground(i2 + mapgen[player][1], mincoorf + mapgen[player][2], { 55,0,55 });
                    if (TCODConsole::root->getChar(i2 + mapgen[player][1], mincoorf + mapgen[player][2]) == 50) {
                        check = 1;
                        break;
                    }
                    if (xcoor < 0) {
                        mincoorf = 0 - mincoorf;
                    }
                    if (ycoor < 0) {
                        i2 = 0 - i2;
                    }
                }
                mincoor -= sub;
            }
            if (check == 0) {
                TCODConsole::root->setChar(mapgen[i][1], mapgen[i][2], mapgen[i][0]);
            }
        }
        
        TCODConsole::root->flush();
        TCOD_key_t key;
        while (true) {
            TCODSystem::checkForEvent(TCOD_EVENT_KEY, &key, NULL);
            check2 = 0;
            TCODSystem::waitForEvent(TCOD_EVENT_ANY, &key, NULL, 0);
            switch (key.vk) {
            case TCODK_DOWN:  hitbox(0, 1);   break;
            case TCODK_UP:    hitbox(0, -1);   break;
            case TCODK_LEFT:  hitbox(-1, 0);   break;
            case TCODK_RIGHT: hitbox(1, 0);   break;
            }
            if (check2 == 1) {
                break;
            }
        }
        if (rand(5000) == 0) {
            check = 1;
            while (check == 1) {
                std::pair<int, int> time = randcoor(50, 100);
                comp(time.first, time.second);
                if (check == 0) {
                    gen(time.first, time.second, 84, 255, 0, 0);
                }
            }
        }
        //Pathfinding
        for (int i = 0; i < mapgen.size(); i++) {
            if (mapgen[i][0] == 84) {
                if (mapgen[i][1] <= mapgen[player][1] && mapgen[i][2] <= mapgen[player][2]) {
                    int ydist = mapgen[i][1] - mapgen[player][1];
                    int xdist = mapgen[i][2] - mapgen[player][2];
                    if (ydist == 0) {
                        comp(mapgen[i][2] + 1, mapgen[i][2]);
                        if (check == 0) {
                            mapgen[i][2] += 1;
                        }
                    }
                    else if (xdist == 0) {
                        comp(mapgen[i][1] + 1, mapgen[i][2]);
                        if (check == 0) {
                            mapgen[i][1] += 1;
                        }
                    }
                    else {
                        std::pair<int, int> location = randcoor(ydist, xdist);
                        if (location.first > location.second) {
                            comp(mapgen[i][1] + 1, mapgen[i][2]);
                            if (check == 0) {
                                mapgen[i][1] += 1;
                            }
                        }
                        else if (location.first == location.second) {
                            if (rand(1) == 0) {
                                comp(mapgen[i][1] + 1, mapgen[i][2]);
                                if (check == 0) {
                                    mapgen[i][1] += 1;
                                }
                            }
                            else {
                                comp(mapgen[i][1], mapgen[i][2] + 1);
                                if (check == 0) {
                                    mapgen[i][2] += 1;
                                }
                            }
                        }
                        else {
                            comp(mapgen[i][1], mapgen[i][2] + 1);
                            if (check == 0) {
                                mapgen[i][2] += 1;
                            }
                        }
                    }
                }
                else if (mapgen[i][1] > mapgen[player][1] && mapgen[i][2] < mapgen[player][2]) {
                    int ydist = mapgen[player][1] - mapgen[i][1];
                    int xdist = mapgen[i][2] - mapgen[player][2];
                    std::pair<int, int> location = randcoor(ydist, xdist);
                    if (location.first > location.second) {
                        comp(mapgen[i][1] - 1, mapgen[i][2]);
                        if (check == 0)
                            mapgen[i][1] -= 1;
                    }
                    else if (location.first == location.second) {
                        if (rand(1) == 0) {
                            comp(mapgen[i][1] - 1, mapgen[i][2]);
                            if (check == 0)
                                mapgen[i][1] -= 1;
                        }
                        else {
                            comp(mapgen[i][1], mapgen[i][2] + 1);
                            if (check == 0)
                                mapgen[i][2] += 1;
                        }
                    }
                    else {
                        comp(mapgen[i][1], mapgen[i][2] + 1);
                        if (check == 0)
                            mapgen[i][2] += 1;
                    }
                }
                else if (mapgen[i][1] < mapgen[player][1] && mapgen[i][2] > mapgen[player][2]) {
                    int ydist = mapgen[i][1] - mapgen[player][1];
                    int xdist = mapgen[player][2] - mapgen[i][2];
                    std::pair<int, int> location = randcoor(ydist, xdist);
                    if (location.first > location.second) {
                        comp(mapgen[i][1] + 1, mapgen[i][2]);
                        if (check == 0)
                            mapgen[i][1] += 1;
                    }
                    else if (location.first == location.second) {
                        if (rand(1) == 0) {
                            comp(mapgen[i][1] + 1, mapgen[i][2]);
                            if (check == 0)
                                mapgen[i][1] += 1;
                        }
                        else {
                            comp(mapgen[i][1], mapgen[i][2] - 1);
                            if (check == 0)
                                mapgen[i][2] -= 1;
                        }
                    }
                    else {
                        comp(mapgen[i][1], mapgen[i][2] - 1);
                        if (check == 0)
                            mapgen[i][2] -= 1;
                    }
                }
                else if (mapgen[i][1] >= mapgen[player][1] && mapgen[i][2] >= mapgen[player][2]) {
                    int ydist = mapgen[player][1] - mapgen[i][1];
                    int xdist = mapgen[player][2] - mapgen[i][2];
                    if (ydist == 0) {
                        comp(mapgen[i][1], mapgen[i][2] - 1);
                        if (check == 0) {
                            mapgen[i][2] -= 1;
                        }
                    }
                    else if (xdist == 0) {
                        comp(mapgen[i][1] - 1, mapgen[i][2]);
                        if (check == 0) {
                            mapgen[i][1] -= 1;
                        }
                    }
                    else {
                        std::pair<int, int> location = randcoor(ydist, xdist);
                        if (location.first > location.second) {
                            comp(mapgen[i][1] - 1, mapgen[i][2]);
                            if (check == 0)
                                mapgen[i][1] -= 1;
                        }
                        else if (location.first == location.second) {
                            if (rand(1) == 0) {
                                comp(mapgen[i][1] - 1, mapgen[i][2]);
                                if (check == 0)
                                    mapgen[i][1] -= 1;
                            }
                            else {
                                comp(mapgen[i][1], mapgen[i][2] - 1);
                                if (check == 0)
                                    mapgen[i][2] -= 1;
                            }
                        }
                        else {
                            comp(mapgen[i][1], mapgen[i][2] - 1);
                            if (check == 0)
                                mapgen[i][2] -= 1;
                        }
                    }
                }
            }
        }


    }
}

