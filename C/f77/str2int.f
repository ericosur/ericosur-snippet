C comment http://ylchang.blogspot.com/2009/05/fortran-77.html
      integer i
      character*80 str

      write(*,*) 'input a string: '
      read(*,*) str

      read(str,*) i

      write(*,FMT='(A A)') 'the string is: ', str
      write(*,*) 'the integer is: ', i

      stop
      end

