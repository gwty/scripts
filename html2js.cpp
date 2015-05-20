//converts html to js string

#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;
int main(int argc, char* argv[])
{
    ifstream in;
    ofstream out;
    char html[1000];
    char var[]="writeme";
    char js[1000];
    strcpy(js, "var ");
    strcat(js,var);
    strcat(js," = ");
    in.open(argv[1],ios::in);
    out.open(argv[2],ios::out);
    out<<js;
    while(in.getline(html,1000))
    {
        out<<"'";
        out<<html;
        out<<"' + \n";
    }
    out<<" '';\n";
    out<<"document.write(writeme);";

    in.close();
    out.close();

}