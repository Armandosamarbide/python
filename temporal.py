print(titulo,artista,anio,genero)
        print(titulo.get(),artista.get(),anio.get(),genero.get())
        
        cadena = titulo.get()
        patron="^[A-Za-záéíóú]*$"
        
        if(re.match(patron, cadena)):
            con = crear_base()
            cursor = con.cursor()
            #mi_id = int(mi_id)
            data = (titulo.get(), cantidad.get(), precio.get())
            sql = "INSERT INTO productos(producto, cantidad, precio) VALUES(?, ?, ?)"
            cursor.execute(sql, data)
            con.commit()
            producto.set("---")
            actualizar_treeview(tree)
        else:
            print("error en campo producto") */