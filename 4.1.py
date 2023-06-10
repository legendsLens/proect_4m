#def strcounter(s):
   #for sym in set(s):
        #counter = 0
        #for sub_sym in s:
            #if sym == sub_sym:
                #counter += 1
        #print(sym, counter)
            
#strcounter('abckfaa')

def strcounter(s):
    syms_cunter = {}
    for sym in s:
        syms_cunter[sym] = syms_cunter.get(sym, 0) + 1

    for sym, count in syms_cunter.items():
        print(sym, count)
strcounter('abckfaa')


#fdglolgfoifgdlgoflfgo