eks_encrypt_keys.py comes from 3rdparty/tr../tools/par.../

Original version need a common.py as module to run.
(but, python itself has module common, no good)

"go.bat" is a batch file to start compile and zip the result.
"setup.py" is a simple conf python script to apply py2exse.


"keybox.bin" is a file for running. You may issue this:
python eks_encrypt_keys.py --sbk=de9cc9bd1fe51ad61619721a502a04ad --widevine_key=keybox.bin

It should run and generate "eks.dat".

Have tested it against python2.6(win32), python2.7(win32) and
py2exe-0.6.9.win32-py2.7.
