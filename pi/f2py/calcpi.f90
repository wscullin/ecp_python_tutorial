
    subroutine calcpi(samples, pi)
      REAL,INTENT(OUT) :: pi
      INTEGER, INTENT(IN) :: samples
      REAL :: x, y
      INTEGER :: i, inside

      inside = 0

      do i = 1, samples

        call random_number(x)
        call random_number(y)

        if ( x**2 + y**2 <= 1.0D+00 ) then
          inside = inside + 1
        end if 

       end do
       pi = 4.0 * REAL(inside) / REAL(samples)
    end subroutine

