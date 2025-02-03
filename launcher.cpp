#include <cstdlib>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std::string_literals;

std::map<std::string, std::set<std::string>> commands = {
    {"migrate"s, {"migrate"s, "mg"s}},
    {"makemigrations"s, {"makemigrations"s, "mm"s}},

    {"no_run"s, {"stop"s, "sp"s}},
    {"help"s, {"--help"s, "-h"s, "h"s, "help"s}},
    {"not_wait", {"not_wait"s, "nw"s}},

    {"pass_all_to_manage_py", {"-p"s}},
};

const auto&& comand_base = "python blogicum/manage.py"s;

bool validate_command(std::string command)
{
    for(auto&& [command_name, aliases] : commands)
    {
        if(aliases.count(command))
        {
            return true;
        }
    }
    return false;
}

bool validate_commands(std::vector<std::string> commands_arr)
{
    if(commands_arr.empty())
    {
        return true;
    }
    for(auto&& command : commands_arr)
    {
        if(commands["pass_all_to_manage_py"s].count(command))
        {
            return true;
        }
        if(!validate_command(command))
        {
            return false;
        }
    }
    return true;
}

int main(int argc, char *argv[])
{

    bool not_wait = false;
    bool no_run = false;

    std::vector<std::string> custom_commands;

    auto&& programm_name = std::string(argv[0]);

    if(!validate_commands(std::vector<std::string>(argv + 1, argv + argc)))
    {
        std::cout << "Invalid command" << std::endl;
        std::cout << "Usage:" << std::endl;
        std::cout << programm_name << " "s << *commands["makemigrations"s].begin() << " "s << *commands["migrate"s].begin() << std::endl;
        std::cout << programm_name << " "s << *commands["-p"s].begin() << " "s << "createsuperuser"s << std::endl;
        std::cout << "For more information use:" << std::endl;
        std::cout << programm_name << " "s << *commands["help"s].begin() << std::endl;
        std::cout << "Press any key to continue..." << std::endl;
        std::cin.get();
        return 1;
    }

    if (!std::getenv("VIRTUAL_ENV"))
    {
        std::cout << "Virtual environment is not active." << std::endl;
        return 1;
    }

    for (int i = 1; i < argc; i++)
    {
        auto&& current_word = std::string(argv[i]);
        if (commands["no_run"s].count(current_word))
        {
            std::cout << "Server run will not be run by default" << std::endl;
            no_run = true;
            continue;
        }
        if (commands["wait"s].count(current_word))
        {
            std::cout << "Server will wait for input in the end" << std::endl;
            not_wait = true;
            continue;
        }
        if (commands["help"s].count(current_word))
        {
            std::cout << "help"s << " ==vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv=="s << std::endl;
            for(auto&& [command_name, aliases] : commands)
            {
                std::cout << command_name << " ";
                for(auto&& alias : aliases)
                {
                    std::cout << alias << " ";
                }
                std::cout << std::endl;
            }
            std::cout << "help"s << " ==^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^=="s << std::endl;
            continue;
        }
        if (commands["makemigrations"s].count(current_word))
        {
            auto&& comand = comand_base + " makemigrations";
            std::cout << comand << " ==vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv=="s << std::endl;
            system(comand.c_str());
            std::cout << comand << " ==^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^=="s << std::endl;
            continue;
        }
        if (commands["migrate"s].count(current_word))
        {
            auto&& comand = comand_base + " migrate";
            std::cout << comand << " ==vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv=="s << std::endl;
            system(comand.c_str());
            std::cout << comand << " ==^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^=="s << std::endl;
            continue;
        }
        if (commands["pass_all_to_manage_py"s].count(current_word))
        {
            std::string comand = comand_base;

            for (int j = i + 1; j < argc; j++)
            {
                comand += " "s + std::string(argv[j]);
            }

            std::cout << comand << " ==vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv=="s << std::endl;
            system(comand.c_str()); // vvv the rest of code might be unreachable due to CTRL-BREAK exit of django vvv
            std::cout << comand << " ==^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^=="s << std::endl;

        if(!not_wait)
        {
            std::cout << "Press any key to continue..." << std::endl;
            std::cin.get();
        }

            return 0;
        }
    }

    if(!no_run)
    {
        auto&& comand = comand_base + " runserver";

        std::cout << comand << " ==vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv=="s << std::endl;
        system(comand.c_str()); // vvv the rest of code might be unreachable due to CTRL-BREAK exit of django vvv
        std::cout << comand << " ==^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^=="s << std::endl;
    }

    if(!not_wait)
    {
        std::cout << "Press any key to continue..." << std::endl;
        std::cin.get();
    }

    return 0;
}