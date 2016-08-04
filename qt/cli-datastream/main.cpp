#include <QtCore>
#include <QDebug>
//#include <QApplication>
#include <iostream>
#include <QDataStream>
#include <QFile>

using namespace std;

#define FOOFILE "/tmp/foo.dat"

class Foo
{
public:
    Foo();
    ~Foo();

    void setM(int v) {
        m = v;
    }
    int getM() const {
        return m;
    }
    void setN(qint32 v) {
        n = v;
    }
    qint32 getN() const {
        return n;
    }
    void append(const QString& s) {
        sl << s;
    }
    void show() {
        foreach (const QString &str, sl) {
            qDebug() << str;
        }
    }
    void save();
    void load();

    friend QDataStream& operator<<(QDataStream& ds, const Foo& obj);
    friend QDataStream& operator>>(QDataStream& ds, Foo& obj);
private:
    int m = 0x0000dead;
    qint32 n = 0x00c0ffee;
    QString s;
    QStringList sl;
};

Foo::Foo()
{
    s = "hello world";
    sl << "apple" << "ball" << "cat";
}

Foo::~Foo()
{
}

QDataStream& operator<<(QDataStream& ds, const Foo& obj)
{
    ds << obj.m << obj.n << obj.s << obj.sl;
    return ds;
}

QDataStream& operator>>(QDataStream& ds, Foo& obj)
{
    ds >> obj.m >> obj.n >> obj.s >> obj.sl;
    return ds;
}

// save object BarCtrl into file
void Foo::save()
{
    qDebug() << Q_FUNC_INFO;
    QFile file(FOOFILE);
    if (!file.open(QIODevice::WriteOnly)) {
        qDebug() << "write file failed";
        return;
    }
    QDataStream out(&file);
    out << *this;
    file.close();
}

// load object BarCtrl from file
void Foo::load()
{
    qDebug() << Q_FUNC_INFO;
    QFile file(FOOFILE);
    if (!file.open(QIODevice::ReadOnly)) {
        qDebug() << "read file failed";
        return;
    }
    QDataStream out(&file);
    out >> *this;
    file.close();
}

int main(int argc, char *argv[])
{
    Q_UNUSED(argc);
    Q_UNUSED(argv);

    Foo *f = new Foo;
    f->setM(0xaa);
    f->setN(0xdd);
    f->append("dog");
    f->show();
    f->save();
    delete f;

    Foo g;
    g.load();
    cout << hex << g.getM() << " " << g.getN() << endl;
    g.show();

    return 0;
}
