/// file: testid3v2.cpp
//
// g++ -o hell -I/home/rasmus/taglib/include/taglib testid3v2.cpp
// -L/home/rasmus/taglib/lib -ltag
//

#include <stdio.h>
#include <iostream>

#include <tmap.h>
#include <tstring.h>
#include <tpropertymap.h>

#include <mpegfile.h>
#include <id3v2tag.h>
#include <id3v2frame.h>
#include <attachedpictureframe.h>

#define FNAME   "/home/rasmus/Music/last.mp3"
#define PICNAME "output.jpg"

using namespace std;

int main(int argc, char** argv)
{
    string fname;
    if (argc == 2) {
        fname = argv[1];
    } else {
        cout << "no file specified, use default...\n";
        fname = FNAME;
    }
    cout << "try this: " << fname << endl;
    TagLib::MPEG::File file(fname.c_str());
    if (!file.isValid()) {
        cout << "invalid!" << endl;
        return -1;
    }

    TagLib::ID3v2::Tag *tag = file.ID3v2Tag(true);
    if (tag == NULL) {
        cout << "no tag, exit..." << endl;
        return -1;
    }

    TagLib::PropertyMap pm(tag->properties());
    TagLib::String s = pm.toString();

    cout << tag->title().toCString(true) << endl
        << tag->album().toCString(true) << endl
        << tag->artist().toCString(true) << endl
        << s.toCString(true) << endl;

    // frames
    TagLib::ID3v2::FrameList frames;
    //look for picture frames
    frames = tag->frameListMap()["APIC"];
    if (frames.isEmpty()) {
        cout << "frmaes is empty" << endl;
    } else {
        TagLib::ID3v2::FrameList::ConstIterator it = frames.begin();
        for(; it != frames.end() ; it++)
        {
            //cast Frame * to AttachedPictureFrame*
            TagLib::ID3v2::AttachedPictureFrame *pictureFrame =
                static_cast<TagLib::ID3v2::AttachedPictureFrame *> (*it);

            //Warning. format of picture assumed to be jpg. This may be false, for example it may be png.
            FILE *fout = fopen(PICNAME, "wb");
            if (fout == NULL) {
                return -1;
            }
            cout << "processing the file "<< FNAME << endl;
            fwrite(pictureFrame->picture().data(), pictureFrame->picture().size(), 1, fout);
            fclose(fout);
            cout << "The picture has been written to " << PICNAME << endl;
            cout << "Remember that the file type .jpg is just assumed for simplicity" << endl;
        }
    }

    return 0;
}
