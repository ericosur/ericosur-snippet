#ifndef MYTRANSLATION_HPP
#define MYTRANSLATION_HPP

#include <QApplication>
#include <QDebug>
#include <QObject>
#include <QTranslator>

class MyTranslation : public QObject
{
    Q_OBJECT
    Q_PROPERTY(QString empty READ getEmptyString NOTIFY languageChanged)

public:
    MyTranslation() {
        //m1 = NULL;
        //m2 = NULL; // new QTranslator;
    }

    ~MyTranslation() {
        //delete m1;
        //delete m2;
    }

    QString getEmptyString() {
        return "";
    }

    Q_INVOKABLE void selectLanguage(QString language) {
        bool ret;
        qDebug() << "selectLanguage(): " << language;
        QTranslator *t = new QTranslator;

        if(language == QString("fr")) {
            //if (m1) qApp->removeTranslator(m1);
            //if (m2) qApp->removeTranslator(m2);
            ret = t->load(":/lang_fr_FR.qm");
            qApp->installTranslator(t);
        }

        if(language == QString("zh")) {
            //if (m1 == NULL)  m1 = new QTranslator;
            ret = t->load(":/lang_zh_TW.qm");
            qApp->installTranslator(t);
        }

        if(language == QString("en")) {
            //if (m2 == NULL)  m2 = new QTranslator;
            //qDebug() << "load en...";
            t->load(":/lang_en_US.qm");
            ret = qApp->installTranslator(t);

            //qApp->removeTranslator(m_trans1);
            //qApp->removeTranslator(m_trans2);
        }

        Q_ASSERT(ret);

        emit languageChanged();
    }

    signals:
        void languageChanged();

    private:
        //QTranslator *m1;
        //QTranslator *m2;
};

#endif // MYTRANSLATION_HPP

