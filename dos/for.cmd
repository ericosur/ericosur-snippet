@echo off
: FOR /F "tokens=*" %%a in (input.txt) do @echo %%a

rem ��@���ɮפ����C���ɮװ�����w���R�O�C
rem
rem FOR %variable IN (set) DO �R�O [command-parameters]
rem
rem   %variable ���w�@�ӥi�H���N���ѼơC
rem   (set)      ���w�Ѥ@�Φh���ɮײզ����ɮײաC�z�i�ϥγq�t�r���C
rem   command    ���w�R�O�Ӱ���C�@���ɮסC
rem  command-parameters
rem              ���ҫ��w���R�O���w�ܼƩΰѼơC
rem
rem �p�G�n�b�妸�{�����ϥ� FOR �R�O�A�Ы��w %%variable�A�Ӥ��n���w
rem %variable�C  �ܼƦW�٦��j�p�g���Ϥ��A�ҥH %i ���P�� %I�C
rem
rem �p�G�z�ҥ��X�R�R�O�A�h�B�~�䴩�U�C�� FOR �R�O
rem �榡:
rem
rem FOR /D %variable IN (set) DO command  [command-parameters]
rem
rem     �p�G set ���]�t�U�Φr���A�h���w�P�ؿ�
rem     �W�٬۲šA�Ӥ��O�P�ɮצW�٬۲šC
rem
rem FOR /R [[drive:]path] %variable IN (set) DO command  [command-parameters]
rem
rem     �b�𪬥ؿ������� [drive:]���|�A�é�𪬥ؿ����C�@�ӥؿ��U����
rem     FOR ���z���C�p�G���b /R ������w�ؿ��W��A�h�ĥΥثe���ؿ��C
rem     �p�G set �u�O��@�y�I (.) �r���A�h���u�|�C�|�𪬥ؿ����c�C
rem

for /l %%a in (1,3,99) do @echo %%a

rem FOR /L %variable IN (start,step,end) DO command [command-parameters]
rem
rem     set �O�q�}�Y�쵲���@�����@�B���s��Ʀr�C�ҥH (1,1,5) �|����
rem     �s��� (1 2 3 4 5) �� (5,-1,1) �|���ͳs��� (5 4 3 2 1)
rem
rem FOR /F ["options"] %variable IN (file-set) DO command [command-parameters]
rem FOR /F ["options"] %variable IN ("string") DO command [command-parameters]
rem FOR /F ["options"] %variable IN ('command') DO command [command-parameters]
rem
rem     �ΡA�p�G�ϥ� usebackq �ﶵ:
rem
rem FOR /F ["options"] %variable IN (file-set) DO command [command-parameters]
rem FOR /F ["options"] %variable IN ('string') DO command [command-parameters]
rem FOR /F ["options"] %variable IN (`command`) DO command [command-parameters]
rem
rem     filenameset �i�H�O�@�ӥH�W���ɮצW�١C�C���ɮ׳��w�}�ҡA
rem     Ū���γB�z�L�A�~�~��i��U���ɮצW�ٲաC�B�z�ɮ�Ū�����@�P
rem     �ʡA�N�������W�ߪ���r��A�M��N�C�@����R���s�Χ�h���r��C
rem     �Τw��쪺�r��Ȭ��ܼƭȡA�өI�s For �j�骺���e�C�w�]���A�A
rem     /F �ǥX�C���ɮת��C�@�椤�A�H�Ů���j���Ĥ@�Ӧr��C�ťզ�
rem     �|�Q���L�C�z�i�H���w "options" �Ѽƨ��мg�w�]�����R�欰�C
rem     �o�O���޸����r��A�]�t�@�ӥH�W������r�A�ӫ��w���P�����R
rem     �ﶵ�C����r�O:
rem
rem         eol=c           - ���w�@�Ӧ�����Ѧr��
rem                           (�u���@��)
rem         skip=n          - ���w�b�ɮ׶}�Y�n���L��
rem                           ��ơC
rem         delims=xxx      - ���w���j�Ÿ������X�C  �o�|���N
rem                           �w�]���ťջP�w��r�������j�Ÿ����X�C
rem         tokens=x,y,m-n  - ���w�C�@�檺���Ǥ�r�����ӳQ
rem                           �Ǩ� for �������H�ΨӶi��C�@�ӭ��ƾާ@�C
rem                           �o�|�ɭP�B�~���ܼƦW�ٳQ�t�m�C
rem                           m-n �榡�N��@�ӽd��A
rem                           ���w�F�� m �Ө�� n �Ӧr�궵�C
rem                           �p�G�b tokens= �r�ꪺ�̫�@�Ӧr���O
rem                           �P���A�h�|�t�m�@���B�~���ܼ�
rem                           �ӱ����̫�@�Ӧr�궵�Q���R��
rem                           ����L��r�C
rem         usebackq        - ���w�s�y�q�}�l�@�ΡC
rem                           �䤤�ϬA�����r��|�Q��@�R�O�Ӱ���A
rem                           �ӳ�޸��r��O�¤�r�r��C
rem                           ���~�٤��\�ϥ����޸���
rem                           �ޥΦb filenameset ��
rem                           ���ɦW�C
rem
rem     �H�U�O�@�ӽd��:
rem
rem FOR /F "eol=; tokens=2,3* delims=, " %i in (myfile.txt) do @echo %i %j %k
rem
rem     �o�|���R myfile.txt �ɮפ����C�@��A�����|�h�ޥH�����}�Y�����
rem     �A�����N�� 2 �Ӥβ� 3 �ӻy�k�q�C�@��Ǩ� for �D��A�Ө�y�k�O
rem     �γr���M/�ΪŮ���}���C�Ъ`�N�Afor �D�鳯�z���ѷ� %i �H���o��
rem     �G�ӻy�k�A�ѷ� %j �H���o�ĤT�ӻy�k�A�ϥ� %k ���o�ĤT�ӻy�k��
rem     �᪺�Ѿl�r��C�]���ɮצW�٧t���Ů�A�z���������޸��ӬA���ɮצW
rem     �١C�n�o�˨ϥ����޸��A�z�����ϥ� usebackq �ѼơC�_�h���޸��|�Q
rem     ��Ķ���Ψөw�q�@���r�C
rem
rem     �ϥ� %i ���զa�b for ���z�����ŧi�A�óz�L tokens= option �ϥ�
rem     %j �@�t���ʪ��ŧi�C�z�i�H�ǥ� tokens= line �ӫ��w�̦h 26 �ӻy
rem     �k�A�e���O���ŧi���ܼƤ��ప��r�� 'z' �� 'Z'�C�аO��AFOR ��
rem     �ƬO��@�r�����A�P�ɦb���@�ɶ����A�z����P�ɨϥζW�L 52 �� FOR
rem     �ܼơC
rem
rem     �z�]�i�H�ϥ� FOR /F �R�O�b�ߧY�r�ꤤ���R�޿�A��k�O�N�A��������
rem     filenameset �ܦ��@�Ӥ޸��r��C���|�Q�����q�ɮ׿�J�����A�å[
rem     �H���R�C
rem
rem     �̫�A�z�i�H�ϥ� FOR /F �R�O�Ӥ��R�@�өR�O����X�C��k�O�N�A��
rem     ���� filenameset �ܦ���޸��r��C���N�Q�����@�өR�O�C�A�o�өR�O
rem     ��N�|�Ǩ�l CMD.EXE�A�ӿ�X�N�|�Q�^����O���餤�A���ɮרӤ�
rem     �R�C�ҥH�U�C���d��:
rem
rem         FOR /F "delims==" %i IN ('set') DO @echo %i
rem
rem     �N�C�|�ثe���Ҥ��������ܼƦW�١C
rem
rem ���~�A�w�g�[�j�F FOR �ܼưѦҪ����N�\��C
rem �z�{�b�i�H��ΤU�C���y�k:
rem
rem     %~I         - �i�} %I �B�����]�򪺤޸� (")
rem     %~fI        - �i�} %I ���@�ӧ����ŦX�����|�W��
rem     %~dI        - �u�i�} %I ���Ϻо��N��
rem     %~pI        - �u�i�} %I �����|
rem     %~nI        - �u�i�} %I ���ɦW
rem     %~xI        - �u�i�} %I �����ɦW
rem     %~sI        - �i�}�����|�u�]�t�u�ɦW
rem     %~aI        - �i�} %I ���ɮת��ɮ��ݩ�
rem     %~tI        - �i�} %I ���ɮת����/�ɶ�
rem     %~zI        - �i�} %I �ɮת�����
rem     %~$PATH:I   - �j�M�Ҧ��C�b PATH �����ܼƤ����ؿ�
rem                    �B�i�} %I ��
rem                    �Ĥ@�ӧ�쪺�����ŦX�ɦW�C
rem                    �p�G�S���w�q�����ܼƦW��
rem                    �άO�j�M�䤣���ɮסA
rem                    �h�o�ӭ׹����|�i�}��
rem                    �Ŧr��C
rem
rem �׹����i�H�X�֨ϥΥH��o��X�����G:
rem
rem     %~dpI       - �u�i�} %I ���Ϻо��N���P���|
rem     %~nxI       - �u�i�} %I ���ɦW�P���ɦW
rem     %~fsI       - �u�i�} %I ���t�u�ɦW���������|
rem     %~dp$PATH:i - �� %I �j�M�Ҧ��C�b PATH �����ܼƤ����ؿ�
rem                    �B�i�}�Ĥ@�ӧ�쪺���ج��Ϻо��N����
rem                    ���|�C
rem     %~ftzaI     - �i�} %I ���� DIR �@�˪���X��
rem
rem �b�W�����d�Ҥ� %I �M PATH ��Ψ�L���X�k�Ȩ��N�C%~ �y�k�O�ѦX�k��
rem FOR �ܼƦW�٨Ӳפ�C�p�G��ι� %I ���j�g�W�٥i�H�W�[�iŪ�ʦӥB�קK
rem �M�׹������V�c�A�]���o�Ǩä��Ϥ��j�p�g�C
