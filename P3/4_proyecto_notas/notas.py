from conexionBD import *
import datetime
def crear(usuario_id, titulo, descripcion):
    try:
        cursor.execute("insert into notas(usuario_id,descripcion,fecha) " \
        "values (%s,%s,%s,NOW())",(usuario_id, titulo, descripcion))
        conexion.commit()
        return True
    except:
        return False
    
def mostrar(usuario_id):
    try:
        cursor.execute("select * from notas where usuario_id=%s",(usuario_id,))
        return cursor.fetchall()
        
    except:
            return []
    
def cambiar(id_titulo,descripcion):
    try:
      cursor.execute("update notas set titulo=%s, descripcion=%s, fecha=NOW() where id=%s", (titulo,descripcion,id_titulo))
      where id=%s",(descripcion,id_titulo))
      conexion.commmit()  
      return True  

     except:
       return False
    
def borrar():
    try:
        cursor.execute("delte from notas where id=%s",(id,))
        conexion.comit()
        
