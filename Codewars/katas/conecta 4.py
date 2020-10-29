col_a = []
col_b = []
col_c = []
col_d = []
col_e = []
col_f = []
col_g = []
ganador=[False,False]
def who_is_winner(pieces_position_list):
    print("Añadimos las fichas")
    for item in pieces_position_list:
        print("Colocamos cada ficha")
        if item[0] == "A" or item[0] == "a":
            col_a.append(item[2:])
        
        elif item[0] == "B" or item[0] == "b":
            col_b.append(item[2:])
        
        elif item[0] == "C" or item[0] == "c":
            col_c.append(item[2:])
        
        elif item[0] == "D" or item[0] == "d":
            col_d.append(item[2:])
        
        elif item[0] == "E" or item[0] == "e":
            col_e.append(item[2:])
        
        elif item[0] == "F" or item[0] == "f":
            col_f.append(item[2:])
        
        elif item[0] == "G" or item[0] == "g":
            col_g.append(item[2:])
            
        col_a_item = 0
        col_b_item = 0
        col_c_item = 0
        col_d_item = 0
        col_e_item = 0
        col_f_item = 0
        col_g_item = 0
        print("Calculamos vacios")
        for item in col_a:
            col_a_item += 1
        for item in col_b:
            col_b_item += 1
        for item in col_c:
            col_c_item += 1
        for item in col_d:
            col_d_item += 1
        for item in col_e:
            col_e_item += 1
        for item in col_f:
            col_f_item += 1
        for item in col_g:
            col_g_item += 1
        
        col_a_vac = 6 - col_a_item
        col_b_vac = 6 - col_b_item
        col_c_vac = 6 - col_c_item
        col_d_vac = 6 - col_d_item
        col_e_vac = 6 - col_e_item
        col_f_vac = 6 - col_f_item
        col_g_vac = 6 - col_g_item
        
        print("Introducimos vacios")
        while col_a_vac > 0:
            col_a.append("X")
            col_a_vac -= 1
        while col_b_vac > 0:
            col_b.append("X")
            col_b_vac -= 1
        while col_c_vac > 0:
            col_c.append("X")
            col_c_vac -= 1
        while col_d_vac > 0:
            col_d.append("X")
            col_d_vac -= 1
        while col_e_vac > 0:
            col_e.append("X")
            col_e_vac -= 1
        while col_f_vac > 0:
            col_f.append("X")
            col_f_vac -= 1
        while col_g_vac > 0:
            col_g.append("X")
            col_g_vac -= 1
        
        #print("==================================================")
        #print(f"A:  {col_a}")
        #print(f"B:  {col_b}")
        #print(f"C:  {col_c}")
        #print(f"D:  {col_d}")
        #print(f"E:  {col_e}")
        #print(f"F:  {col_f}")
        #print(f"G:  {col_g}")
        #print("==================================================")
            
        Condiciones()
        
        print("Eliminamos vacios")
        
        for item in col_a:
            if item == "X":
                col_a_vac += 1
        for item in col_b:
            if item == "X":
                col_b_vac += 1
        for item in col_c:
            if item == "X":
                col_c_vac += 1
        for item in col_d:
            if item == "X":
                col_d_vac += 1
        for item in col_e:
            if item == "X":
                col_e_vac += 1
        for item in col_f:
            if item == "X":
                col_f_vac += 1
        for item in col_g:
            if item == "X":
                col_g_vac += 1
        
        while col_a_vac > 0:
            col_a.remove("X")
            col_a_vac -= 1
        while col_b_vac > 0:
            col_b.remove("X")
            col_b_vac -= 1
        while col_c_vac > 0:
            col_c.remove("X")
            col_c_vac -= 1
        while col_d_vac > 0:
            col_d.remove("X")
            col_d_vac -= 1
        while col_e_vac > 0:
            col_e.remove("X")
            col_e_vac -= 1
        while col_f_vac > 0:
            col_f.remove("X")
            col_f_vac -= 1
        while col_g_vac > 0:
            col_g.remove("X")
            col_g_vac -= 1
        
        print("==================================================")
        print(f"A:  {col_a}")
        print(f"B:  {col_b}")
        print(f"C:  {col_c}")
        print(f"D:  {col_d}")
        print(f"E:  {col_e}")
        print(f"F:  {col_f}")
        print(f"G:  {col_g}")
        print("==================================================")
        
        #Comprobar ganador
        if ganador[0] == True and ganador[1] == False:
            
            return("Yellow")
        elif ganador[0] == False and ganador[1] == True:
            return("Red")
        elif ganador[0] == True and ganador[1] == True:
            print("Error CRITICO")
        print("T")
        print("T")
        print("T")
        print("T")
    return("Draw")
            
            
            
            
        
        
def Condiciones():
    print("Comprobando condiciones")
    e = "Yellow"
    if col_a[0] == e and col_a[1] == e and col_a[2] == e and col_a[3] == e or col_a[1] == e and col_a[2] == e and col_a[3] == e and col_a[4] == e or col_a[2] == e and col_a[3] == e and col_a[4] == e and col_a[5] == e or col_b[0] == e and col_b[1] == e and col_b[2] == e and col_b[3] == e or col_b[1] == e and col_b[2] == e and col_b[3] == e and col_b[4] == e or col_b[2] == e and col_b[3] == e and col_b[4] == e and col_b[5] == e or col_c[0] == e and col_c[1] == e and col_c[2] == e and col_c[3] == e or col_c[1] == e and col_c[2] == e and col_c[3] == e and col_c[4] == e or col_c[2] == e and col_c[3] == e and col_c[4] == e and col_c[5] == e or col_d[0] == e and col_d[1] == e and col_d[2] == e and col_d[3] == e or col_d[1] == e and col_d[2] == e and col_d[3] == e and col_d[4] == e or col_d[2] == e and col_d[3] == e and col_d[4] == e and col_d[5] == e or col_e[0] == e and col_e[1] == e and col_e[2] == e and col_e[3] == e or col_e[1] == e and col_e[2] == e and col_e[3] == e and col_e[4] == e or col_e[2] == e and col_e[3] == e and col_e[4] == e and col_e[5] == e or col_f[0] == e and col_f[1] == e and col_f[2] == e and col_f[3] == e or col_f[1] == e and col_f[2] == e and col_f[3] == e and col_f[4] == e or col_f[2] == e and col_f[3] == e and col_f[4] == e and col_f[5] == e or col_g[0] == e and col_g[1] == e and col_g[2] == e and col_g[3] == e or col_g[1] == e and col_g[2] == e and col_g[3] == e and col_g[4] == e or col_g[2] == e and col_g[3] == e and col_g[4] == e and col_g[5] == e:
        ganador[0]=True
        ganador[1]=False
        print("Condicion 1 " + e)
        return(e)
    k = 0
    while k < 5:
        if col_a[k] == e and col_b[k] == e and col_c[k] == e and col_d[k] == e or col_e[k] == e and col_b[k] == e and col_c[k] == e and col_d[k] == e or col_e[k] == e and col_f[k] == e and col_c[k] == e and col_d[k] == e or col_e[k] == e and col_f[k] == e and col_g[k] == e and col_d[k] == e:
            ganador[0]=True
            ganador[1]=False
            print("Condicion 2 " + e)
            return(e)
        k +=1
    if col_a[2] == e and col_b[3] == e and col_c[4] == e and col_d[5] == e or col_a[0] == e and col_b[1] == e and col_c[2] == e and col_d[3] == e or col_b[1] == e and col_c[2] == e and col_d[3] == e and col_e[4] == e or col_c[2] == e and col_d[3] == e and col_e[4] == e and col_f[5] == e or col_b[0] == e and col_c[1] == e and col_d[2] == e and col_e[3] == e or col_c[1] == e and col_d[2] == e and col_e[3] == e and col_f[4] == e or col_d[2] == e and col_e[3] == e and col_f[4] == e and col_g[5] == e or col_d[0] == e and col_e[1] == e and col_f[2] == e and col_g[3] == e or col_c[0] == e and col_d[1] == e and col_e[2] == e and col_f[3] == e or col_d[1] == e and col_e[2] == e and col_f[3] == e and col_g[4] == e or col_a[1] == e and col_b[2] == e and col_c[3] == e and col_d[4] == e or col_b[2] == e and col_c[3] == e and col_d[4] == e and col_e[5] == e:
        ganador[0]=True
        ganador[1]=False
        print("Condicion 3 " + e)
        return(e)
    elif col_g[2] == e and col_f[3] == e and col_e[4] == e and col_d[5] == e or col_g[0] == e and col_f[1] == e and col_e[2] == e and col_d[3] == e or col_f[1] == e and col_e[2] == e and col_d[3] == e and col_c[4] == e or col_e[2] == e and col_d[3] == e and col_c[4] == e and col_b[5] == e or col_f[0] == e and col_e[1] == e and col_d[2] == e and col_c[3] == e or col_e[1] == e and col_d[2] == e and col_c[3] == e and col_b[4] == e or col_d[2] == e and col_c[3] == e and col_b[4] == e and col_a[5] == e or col_d[0] == e and col_c[1] == e and col_b[2] == e and col_a[3] == e or col_e[0] == e and col_d[1] == e and col_c[2] == e and col_b[3] == e or col_d[1] == e and col_c[2] == e and col_b[3] == e and col_a[4] == e or col_g[1] == e and col_f[2] == e and col_e[3] == e and col_d[4] == e or col_f[2] == e and col_e[3] == e and col_d[4] == e and col_c[5] == e:
        ganador[0]=True
        ganador[1]=False
        print("Condicion 4 " + e)
        return(e)
    e = "Red"
    if (col_a[0] == e and col_a[1] == e and col_a[2] == e and col_a[3] == e or col_a[1] == e and col_a[2] == e and col_a[3] == e and col_a[4] == e or col_a[2] == e and col_a[3] == e and col_a[4] == e and col_a[5] == e or col_b[0] == e and col_b[1] == e and col_b[2] == e and col_b[3] == e or col_b[1] == e and col_b[2] == e and col_b[3] == e and col_b[4] == e or col_b[2] == e and col_b[3] == e and col_b[4] == e and col_b[5] == e or col_c[0] == e and col_c[1] == e and col_c[2] == e and col_c[3] == e or col_c[1] == e and col_c[2] == e and col_c[3] == e and col_c[4] == e or col_c[2] == e and col_c[3] == e and col_c[4] == e and col_c[5] == e or col_d[0] == e and col_d[1] == e and col_d[2] == e and col_d[3] == e or col_d[1] == e and col_d[2] == e and col_d[3] == e and col_d[4] == e or col_d[2] == e and col_d[3] == e and col_d[4] == e and col_d[5] == e or col_e[0] == e and col_e[1] == e and col_e[2] == e and col_e[3] == e or col_e[1] == e and col_e[2] == e and col_e[3] == e and col_e[4] == e or col_e[2] == e and col_e[3] == e and col_e[4] == e and col_e[5] == e or col_f[0] == e and col_f[1] == e and col_f[2] == e and col_f[3] == e or col_f[1] == e and col_f[2] == e and col_f[3] == e and col_f[4] == e or col_f[2] == e and col_f[3] == e and col_f[4] == e and col_f[5] == e or col_g[0] == e and col_g[1] == e and col_g[2] == e and col_g[3] == e or col_g[1] == e and col_g[2] == e and col_g[3] == e and col_g[4] == e or col_g[2] == e and col_g[3] == e and col_g[4] == e and col_g[5] == e):
        ganador[0]=False
        ganador[1]=True
        print("Condicion 1 " + e)
        return(e)
    k = 0
    while k < 5:
        if col_a[k] == e and col_b[k] == e and col_c[k] == e and col_d[k] == e or col_e[k] == e and col_b[k] == e and col_c[k] == e and col_d[k] == e or col_e[k] == e and col_f[k] == e and col_c[k] == e and col_d[k] == e or col_e[k] == e and col_f[k] == e and col_g[k] == e and col_d[k] == e:
            ganador[0]=False
            ganador[1]=True
            print("Condicion 2 " + e)
            return(e)
        k +=1
    if col_a[2] == e and col_b[3] == e and col_c[4] == e and col_d[5] == e or col_a[0] == e and col_b[1] == e and col_c[2] == e and col_d[3] == e or col_b[1] == e and col_c[2] == e and col_d[3] == e and col_e[4] == e or col_c[2] == e and col_d[3] == e and col_e[4] == e and col_f[5] == e or col_b[0] == e and col_c[1] == e and col_d[2] == e and col_e[3] == e or col_c[1] == e and col_d[2] == e and col_e[3] == e and col_f[4] == e or col_d[2] == e and col_e[3] == e and col_f[4] == e and col_g[5] == e or col_d[0] == e and col_e[1] == e and col_f[2] == e and col_g[3] == e or col_c[0] == e and col_d[1] == e and col_e[2] == e and col_f[3] == e or col_d[1] == e and col_e[2] == e and col_f[3] == e and col_g[4] == e or col_a[1] == e and col_b[2] == e and col_c[3] == e and col_d[4] == e or col_b[2] == e and col_c[3] == e and col_d[4] == e and col_e[5] == e:
        ganador[0]=False
        ganador[1]=True
        print("Condicion 3 " + e)
        return(e)
    elif col_g[2] == e and col_f[3] == e and col_e[4] == e and col_d[5] == e or col_g[0] == e and col_f[1] == e and col_e[2] == e and col_d[3] == e or col_f[1] == e and col_e[2] == e and col_d[3] == e and col_c[4] == e or col_e[2] == e and col_d[3] == e and col_c[4] == e and col_b[5] == e or col_f[0] == e and col_e[1] == e and col_d[2] == e and col_c[3] == e or col_e[1] == e and col_d[2] == e and col_c[3] == e and col_b[4] == e or col_d[2] == e and col_c[3] == e and col_b[4] == e and col_a[5] == e or col_d[0] == e and col_c[1] == e and col_b[2] == e and col_a[3] == e or col_e[0] == e and col_d[1] == e and col_c[2] == e and col_b[3] == e or col_d[1] == e and col_c[2] == e and col_b[3] == e and col_a[4] == e or col_g[1] == e and col_f[2] == e and col_e[3] == e and col_d[4] == e or col_f[2] == e and col_e[3] == e and col_d[4] == e and col_c[5] == e:
        ganador[0]=False
        ganador[1]=True
        print("Condicion 4 " + e)
        return(e)

if __name__ == "__main__":
    assert(who_is_winner([ "C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow", "G_Red", "C_Yellow", "C_Red","D_Yellow", "F_Red", "E_Yellow", "A_Red", "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red", "B_Yellow", "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"]), "Yellow")

    assert(who_is_winner(["C_Yellow", "B_Red", "B_Yellow", "E_Red", "D_Yellow", "G_Red", "B_Yellow", "G_Red", "E_Yellow", "A_Red", "G_Yellow", "C_Red", "A_Yellow", "A_Red", "D_Yellow", "B_Red", "G_Yellow", "A_Red", "F_Yellow", "B_Red", "D_Yellow", "A_Red", "F_Yellow", "F_Red", "B_Yellow", "F_Red", "F_Yellow", "G_Red", "A_Yellow", "F_Red", "C_Yellow", "C_Red", "G_Yellow", "C_Red", "D_Yellow", "D_Red", "E_Yellow", "D_Red", "E_Yellow", "C_Red", "E_Yellow", "E_Red"]), "Yellow")
    
    assert(who_is_winner(["F_Yellow", "G_Red", "D_Yellow", "C_Red", "A_Yellow", "A_Red", "E_Yellow", "D_Red", "D_Yellow", "F_Red", "B_Yellow", "E_Red", "C_Yellow", "D_Red", "F_Yellow", "D_Red", "D_Yellow", "F_Red", "G_Yellow", "C_Red", "F_Yellow", "E_Red", "A_Yellow", "A_Red", "C_Yellow", "B_Red", "E_Yellow", "C_Red", "E_Yellow", "G_Red", "A_Yellow", "A_Red", "G_Yellow", "C_Red", "B_Yellow", "E_Red", "F_Yellow", "G_Red", "G_Yellow", "B_Red", "B_Yellow", "B_Red"]), "Red")

    assert(who_is_winner(["A_Yellow", "B_Red", "B_Yellow", "C_Red", "G_Yellow", "C_Red", "C_Yellow", "D_Red", "G_Yellow", "D_Red","G_Yellow", "D_Red", "F_Yellow", "E_Red", "D_Yellow"]), "Red")

    assert(who_is_winner(["A_Red", "B_Yellow", "A_Red", "B_Yellow", "A_Red", "B_Yellow", "G_Red", "B_Yellow"]), "Yellow")

    assert(who_is_winner(["A_Red", "B_Yellow", "A_Red", "E_Yellow", "F_Red", "G_Yellow", "A_Red", "G_Yellow"]), "Draw");