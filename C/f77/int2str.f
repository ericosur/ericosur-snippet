C from http://ylchang.blogspot.com/2009/05/fortran-77.html
      integer i
      character*80 str

      i=1
      write(*,*) 'input a integer: '
      read(*,*) i

      write(str, FMT='(I5)') i

      write(*,*) 'the integer is: ', i
      write(*,FMT='(A A)') 'the string is: ', str

      stop
      end

