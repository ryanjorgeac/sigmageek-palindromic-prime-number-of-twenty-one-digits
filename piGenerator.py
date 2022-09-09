def piGenerator():
    q,r,t,i = 1, 180, 60, 2
    while True:
        u,y = 3*(3*i+1)*(3*i+2), (q*(27*i-12)+5*r)//(5*t)
        yield y
        q,r,t,i = 10*q*i*(2*i-1),10*u*(q*(5*i-2)+r-y*t),t*u,i+1
        
        