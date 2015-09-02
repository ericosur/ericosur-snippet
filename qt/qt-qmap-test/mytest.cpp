#include "mytest.h"

#include <iostream>
#include <QDebug>
#include <QMap>
#include <QHash>
#include <QCache>
#include <QMultiMap>

using namespace std;

QMap<QString, int> _map;

void test_main()
{
    test_multimap();
    test_hash();
}

void test_multimap()
{
    cout << "test_multimap()";
    QMultiMap<QString, int> map1, map2, map3;
    map1.insert("apple", 100);
    map1.insert("apple", 200);
    //cout << map1.size() << endl;
    map2.insert("apple", 300);
    map3 = map1 + map2;

    cout << "apple: " << map1.value("apple") << endl;
    // method #1
  {
    QList<int> values = map3.values("apple");
    int i;
    foreach (i, values) {
        cout << i << "\t";
    }
    cout << endl;
  }

/*
    for (int i = 0; i < values.size(); ++i) {
        cout << values.at(i) << endl;
    }
*/
    // method #2
  {
    QMap<QString, int>::const_iterator i = map3.find("apple");
    while (i != map3.end() && i.key() == "apple") {
        cout << i.value() << "\t";
        ++ i;
    }
    cout << endl;
  }

}

void test_itor()
{
    cout << "test_itor()";
    _map.insert("apple", 137);
    _map.insert("cat", 381);
    _map.insert("jacket", 375);
    _map.insert("moon", 971);
    _map.insert("sun", 411);
    QMap<QString, int>::const_iterator i = _map.find("jacket");
    while (i != _map.end() && i.key() == "jacket") {
        cout << i.value() << endl;
        ++ i;
    }
}

void init_data()
{
    _map["apple"] = 25;
    _map["duck"] = 99;
    _map["horse"] = 1375;
    _map.insert("zebra", 9972);
}

void test_function()
{
    cout << "test_function()";
    //cout << "hello world!" << std::endl;
    //qDebug() << "hell word";

    init_data();
    int m = _map["apple"];
    int n = _map.value("horse");
    //qDebug() << str1 << str2;
    cout << "apple: " << m << endl;
    cout << "horse: " << n << endl;

    /*
    if (_map.contains("cat")) {
        cout << "apple: " << _map.value("apple").toStdString() << std::endl;
    } else {
        cout << "not exists\n";
    }
    */

    QMapIterator<QString, int> it(_map);
    while (it.hasNext()) {
        it.next();
        //cout << it.key().toStdString() << ": " << it.value().toStdString() << endl;
    }

    QMap<QString, int>::const_iterator its = _map.constBegin();
    while (its != _map.constEnd()) {
        //cout << its.key().toStdString() << ": " << its.value().toStdString() << endl;
        ++its;
    }
}

void test_hash()
{
    QMap<QString, int> hh;
    hh.insert("pork", 99);
    hh.insert("beef", 199);
    hh.insert("chicken", 79);
    QList<QString> kl = hh.keys();
    QString ss;
    foreach (ss, kl) {
        cout << "ss: " << ss.toStdString() << "\t";
    }
    cout << endl;
    QList<int> vl = hh.values();
    int ii;
    foreach (ii, vl) {
        cout << "ii: " << ii << "\t";
    }
    cout << endl;
}
