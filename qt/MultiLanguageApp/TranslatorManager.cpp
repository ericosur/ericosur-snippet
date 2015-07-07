#include <QApplication>
#include <QStringList>
#include "TranslatorManager.h"

TranslatorManager* TranslatorManager::m_Instance = 0;

TranslatorManager::TranslatorManager()
{
    QString defaultLang = "en_US";
    QStringList resources;
    resources << "i18n/lang_en_US" << "i18n/lang_fr_FR" << "i18n/lang_ru_RU" << "i18n/lang_zh_TW";

    QStringList languages;
    languages << "en_US" << "fr_FR" << "ru_RU" << "zh_TW";

    for (int j = 0; j < resources.size(); j++)
    {
        QTranslator* pTranslator = new QTranslator;
        if (pTranslator->load(resources[j], ":/"))
        {
            if (languages[j] == defaultLang)
            {
                qApp->installTranslator(pTranslator);
                m_keyLang = languages[j];
            }

            m_translators.insert(languages[j], pTranslator);
        }
    }
}

TranslatorManager::~TranslatorManager()
{
    TranslatorMap::const_iterator i = m_translators.begin();
    while (i != m_translators.end())
    {
        QTranslator* pTranslator = i.value();
        delete pTranslator;
        ++i;
    }

    m_translators.clear();
}

TranslatorManager* TranslatorManager::instance()
{
    static QMutex mutex;
    if (!m_Instance)
    {
        mutex.lock();

        if (!m_Instance)
            m_Instance = new TranslatorManager;

        mutex.unlock();
    }

    return m_Instance;
}

bool TranslatorManager::setTranslator(QString& lang)
{
    bool rc = false;
    if (lang != m_keyLang && m_translators.contains(lang))
    {
        QTranslator* pTranslator = m_translators[m_keyLang];
        QCoreApplication::removeTranslator(pTranslator);
        pTranslator = m_translators[lang];
        QCoreApplication::installTranslator(pTranslator);
        m_keyLang = lang;
        rc = true;
    }

    return rc;
}
