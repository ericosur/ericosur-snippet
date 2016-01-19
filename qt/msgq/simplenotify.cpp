/// file: simplenotify.cpp

#include <QDebug>

#include <unistd.h>
#include <sys/types.h>
#include <sys/inotify.h>
#include <errno.h>

#include "simplenotify.h"

SimpleNotify::SimpleNotify(const QString& watch_file) :
    m_filename(watch_file)
{
}

void SimpleNotify::run()
{
    qDebug() << "SimpleNotify::run()";

    int fd;
    int wd;
    //int length;
    const int BUF_LEN = 512;
    char buffer[BUF_LEN];

    fd = inotify_init();
    if ( fd < 0 ) {
        qDebug() << "SimpleNotify: inotify_init failed";
        return;
    }

    wd = inotify_add_watch( fd, m_filename.toUtf8(), IN_MODIFY | IN_CREATE | IN_DELETE | IN_ATTRIB);
    if (wd < 0) {
        qDebug() << "SimpleNotify: inotify_add_watch failed, errno: " << errno;
        print_errno(errno);
        return;
    }

    // will block at read() here
    (void) read( fd, buffer, BUF_LEN );

    // will go here if file is modified/created/deleted
    qDebug() << "SimpleNotify: emit sigNotify";
    emit sigNotify();

    (void) inotify_rm_watch(fd, wd);
    (void) close(fd);
}

void SimpleNotify::print_errno(int err)
{
    switch (err) {
    case EACCES:
        qDebug() << "EACCES";
        break;
    case EBADF:
        qDebug() << "EBADF";
        break;
    case EFAULT:
        qDebug() << "EFAULT";
        break;
    case EINVAL:
        qDebug() << "EINVAL";
        break;
    case ENAMETOOLONG:
        qDebug() << "ENAMETOOLONG";
        break;
    case ENOENT:
        qDebug() << "ENOENT";
        break;
    case ENOMEM:
        qDebug() << "ENOMEM";
        break;
    case ENOSPC:
        qDebug() << "ENOSPC";
        break;
    }

}
