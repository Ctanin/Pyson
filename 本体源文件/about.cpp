#ifndef ONLINE_JUDGE
#pragma GCC optimize(3)
#include<windows.h>
#endif
#include<iostream>
#include<easyx.h>
using namespace std;
typedef unsigned long long int UL;
typedef long long int LL;
typedef unsigned short US;
IMAGE img1;
int main()
{
    ios::sync_with_stdio(false);
	initgraph(730,460);
	loadimage(&img1,_T("img1.jpg"),310,190,true);
	setbkcolor(WHITE);
	cleardevice();
	settextcolor(BLACK);
	putimage(0,0,&img1);
	settextstyle(40,0,"微软雅黑");
	outtextxy(315,0,"Pyson是什么？");
	settextstyle(25,0,"微软雅黑");
	outtextxy(315,45,"简单来说，Pyson是一门面向结果的高级语言，");
	outtextxy(315,75,"不仅继承了C--中的各种难以理解的包含，格式");
	outtextxy(315,105,"等，还摒弃了Jvav中的各种优点，通常被用于");
	outtextxy(315,135,"大型沙河游戏Minicrash的开发、企业级BBOS");
	outtextxy(315,165,"服务器、MacDOS系统和PPT OS应用程序开发等");
	settextstyle(35,0,"Consolas");
	outtextxy(0,200,"当前版本：Pyson 0.0.0 (Pre-Version) 114-bit");
	settextstyle(25,0,"Consolas");
	outtextxy(0,240,"官方网站：ctanin.github.io/pyson.github.io");
	outtextxy(0,300,"按任意键以退出......");
	getchar();
    return 0;
}

