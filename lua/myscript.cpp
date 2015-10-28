/**
    reference: https://eliasdaler.wordpress.com/2013/10/11/lua_cpp_binder/
**/

#include <iostream>
#include <string>
#include <lua.hpp>

using namespace std;

class MyLua
{
public:
	MyLua() {
        level = 0;
        L = luaL_newstate();
        cout << "lua new state..." << endl;
        cout << "L: " << L << endl;
	}
	~MyLua() {
        if (L) {
            lua_close(L);
            cout << "lua_closed" << endl;
        }
	}

    void show(int ret) {
        cout << "ret = " << ret << endl;
    }

    void load_file(const char* fn) {
        int ret = luaL_dofile(L, fn);
        if (ret) {
            cout << "something wrong..." << endl;
            cout << "error: " << lua_tostring(L, -1) << endl;
        }
    }

    void printError(const string& var, const string& reason) {
        cout << "error: cannot get [" << var << "]. " << reason << endl;
    }

    // generic get
    template<typename T>
    T lua_get(const string& var) {
        return 0;
    }

    // generic default get
    template<typename T>
    T lua_getdefault(const string& var) {
        return 0;
    }

    template<typename T>
    T get(const string& var) {
        if(!L) {
            printError(var, "Script is not loaded");
            return lua_getdefault<T>();
        }

        T result;
        if (lua_gettostack(var)) { // variable succesfully on top of stack
            result = lua_get<T>(var);
        } else {
            result = lua_getdefault<T>();
        }

        lua_pop(L, level + 1); // pop all existing elements from stack
        return result;
    }

    bool lua_gettostack(const string& var);

private:
	lua_State* L;
    int level;
};


bool MyLua::lua_gettostack(const std::string& variableName) {
  level = 0;
  std::string var = "";
    for(unsigned int i = 0; i < variableName.size(); i++) {
      if(variableName.at(i) == '.') {
        if(level == 0) {
          lua_getglobal(L, var.c_str());
        } else {
          lua_getfield(L, -1, var.c_str());
        }

        if(lua_isnil(L, -1)) {
          printError(variableName, var + " is not defined");
          return false;
        } else {
          var = "";
          level++;
        }
      } else {
        var += variableName.at(i);
      }
    }
    if(level == 0) {
      lua_getglobal(L, var.c_str());
    } else {
      lua_getfield(L, -1, var.c_str());
    }
    if(lua_isnil(L, -1)) {
        printError(variableName, var + " is not defined");
        return false;
    }

    return true;
}

template < >
inline bool MyLua::lua_get(const string& var) {
    return (bool)lua_toboolean(L, -1);
}

template < >
inline float MyLua::lua_get(const string& var) {
    if (!lua_isnumber(L, -1)) {
        printError(var, "not a number");
    }
    return (float)lua_tonumber(L, -1);
}

template < >
inline int MyLua::lua_get(const string& var) {
    if (!lua_isnumber(L, -1)) {
        printError(var, "not a number");
    }
    return (int)lua_tonumber(L, -1);
}

template < >
inline string MyLua::lua_get(const string& var) {
    string s = "null";
    if (lua_isstring(L, -1)) {
        s = string(lua_tostring(L, -1));
    } else {
        printError(var, "Not a string");
    }
    return s;
}

template<>
inline std::string MyLua::lua_getdefault<std::string>() {
  return "null";
}

int main()
{
    MyLua *p = new MyLua;
    cout << "new..." << endl;
    const char* fn = "player.lua";
    p->load_file(fn);
    std::string f = p->get<std::string>("player.filename");
    cout << "f: " << f << endl;
    int x = p->get<int>("player.pos.x");
    cout << "x: " << x << endl;
    delete p;
    return 0;
}
