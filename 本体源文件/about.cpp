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
	settextstyle(40,0,"΢���ź�");
	outtextxy(315,0,"Pyson��ʲô��");
	settextstyle(25,0,"΢���ź�");
	outtextxy(315,45,"����˵��Pyson��һ���������ĸ߼����ԣ�");
	outtextxy(315,75,"�����̳���C--�еĸ����������İ�������ʽ");
	outtextxy(315,105,"�ȣ���������Jvav�еĸ����ŵ㣬ͨ��������");
	outtextxy(315,135,"����ɳ����ϷMinicrash�Ŀ�������ҵ��BBOS");
	outtextxy(315,165,"��������MacDOSϵͳ��PPT OSӦ�ó��򿪷���");
	settextstyle(35,0,"Consolas");
	outtextxy(0,200,"��ǰ�汾��Pyson 0.0.0 (Pre-Version) 114-bit");
	settextstyle(25,0,"Consolas");
	outtextxy(0,240,"�ٷ���վ��ctanin.github.io/pyson.github.io");
	outtextxy(0,300,"����������˳�......");
	getchar();
    return 0;
}

