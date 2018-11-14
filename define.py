#!/usr/bin/python3
def wait(time):
    from time import sleep
    sleep(time)
def ask(txt):
    return(input(txt + '  --->   '))
def say(txt, atxt=None, btxt=None, ctxt=None, dtxt=None, etxt=None, ftxt=None, gtxt=None):
    if atxt is None:
        atxt = ''
    if btxt is None:
        btxt = ''
    if ctxt is None:
        ctxt = ''
    if dtxt is None:
        dtxt = ''
    if etxt is None:
        etxt = ''
    if ftxt is None:
        ftxt = ''
    if gtxt is None:
        gtxt = ''
    print(txt, atxt, btxt, ctxt, dtxt, etxt, ftxt, gtxt)

if __name__ == '__main__':
    hi = "hi"
    print('test')
    say(hi, hi, hi, hi, hi)
    
