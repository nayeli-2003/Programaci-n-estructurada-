from conexionBD import * 

def agregar(id_proveedor,nombre,telefono,email):
    try:
        cursor.execute("insert into proveedor (id_proveedor,nombre,telefono,email) values (%s,%s,%s,%s)",(id_proveedor,nombre,telefono,email))
        conexion.commit()
        return True
    except:
        return False
    
def mostrar(id_proveedor):
    try:
        cursor.execute("select * from proveedor where id_proveedor=%s",(id_proveedor,))
        return cursor.fetchall()
    except:
        return []

def modificar(id_proveedor,nombre,telefono,email):
    try:
        cursor.execute("update proveedor set nombre=%s, telefono=%s, email=%s where id_proveedor=%s",(nombre,telefono,email,id_proveedor))
        conexion.commit()
        return True
    except:
        return False

def borrar(nombre): 
    try:
        cursor.execute("delete from proveedor where nombre=%s",(nombre,))
        conexion.commit()
        return True
    except:
        return False


#def registrar(id_proveedor, nombre, telefono, email):
 #   try:
  #      sql = "INSERT INTO proveedores (id_proveedores, nombre, telefono, email) VALUES (%s, %s, %s, %s)"
   #     val = (id_proveedor, nombre, telefono, email)
    #    cursor.execute(sql, val)
     #   conexion.commit()
      #  return True
    #except Exception as e:
     #    print("Error en el registro:", e) 
      #   return False