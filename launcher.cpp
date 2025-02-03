#include <cstdlib>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <array>
#include <stdexcept>

using namespace std::string_literals;

const auto&& comand_base = "python blogicum/manage.py "s;
const auto&& recompile_clang = "clang launcher.cpp -o launch.exe"s; // windows recomended
const auto&& recompile_gpp = "g++ launcher.cpp -o launch"s; // ubuntu recomended

int main(int argc, char *argv[])
{
    using namespace std;

    if(argc == 1)
    {
        auto comand = comand_base + "runserver"s;
        cout << comand << " ==vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv==" << endl;
        system(comand.c_str());

        cout << "Something went wrong. U was supposed to end process with ctrl+c and never reach tis output.";
        return 1;
    }

    array<string, 4> default_commands = {"(custom command)", "makemigration"s, "migrate"s, "createsuperuser"s};

    int switcher = 0;

    if(argc = 2)
    {
        string arg = argv[1];
        if(arg == "clang"s | arg == "g++")
        {
            cout << "cant recompile on run. copy and paste one of this commands:"s << endl;
            cout << recompile_clang << endl;
            cout << recompile_gpp << endl;
            cout << "g++ recomended for ubuntu, clang - for windows"s << endl;
            return 0;
        }

        try
        {
            switcher = stoi(argv[1]);
            default_commands.at(switcher);
        }
        catch(...)
        {
            cout << "choose variant that would be passed to manage.py:" << endl;
            for(int i = 0; i < default_commands.size(); ++i)
            {
                cout << i << ": "s << default_commands[i] << endl;
            }

            cin >> switcher;
            if (cin.fail() || switcher < 0 || switcher >= default_commands.size())
            {
                cout << "invalid input"s << endl;
                return -1;
            }
        }
    }
    else
    {
        cout << "invalid input"s << endl;
        return -1;
    }
    
    string args;
    if(switcher == 0)
    {
        cout << "enter custom command:" << endl;
        getline(cin, args);
        getline(cin, args);
    }
    else
    {
        args = default_commands.at(switcher);
    }
    auto comand = comand_base + args;
    cout << comand << " ==vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv==" << endl;
    system(comand.c_str());
    cout << comand << " ==^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^==" << endl;
    return 0;
}