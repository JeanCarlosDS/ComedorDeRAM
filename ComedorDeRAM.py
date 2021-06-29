while True: # → Verifica-se sempre, logo o programa ficará preso neste loop.

     argm = []                                                      #
     for w in range(48,123):                                        #
          for y in range(48, 123):                                  #
               for i in range(48, 123):                             #
                    for o in range(48, 123):                        #
                         argm.append(chr(w)+chr(y)+chr(i)+chr(o))   # → Gera cerca de 34 milhões de combinações.

     a = argm
     print(a) # → Imprime os resultados.
