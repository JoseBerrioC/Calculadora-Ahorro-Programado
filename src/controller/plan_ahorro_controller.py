import sys
sys.path.append(".")
sys.path.append("src")

import psycopg2
from model.plan_ahorro import PlanAhorro
import secret_config

class PlanAhorroController:

    @classmethod
    def obtener_cursor(cls):
        """Crea la conexión a la base de datos PostgreSQL usando secret_config."""
        conexion = psycopg2.connect(
            database=secret_config.PGDATABASE,
            user=secret_config.PGUSER,
            password=secret_config.PGPASSWORD,
            host=secret_config.PGHOST,
            port=secret_config.PGPORT
        )
        return conexion.cursor()

    @classmethod
    def crear_tabla(cls):
        """Ejecuta el script SQL para crear la tabla planes_ahorro."""
        cursor = cls.obtener_cursor()
        with open("sql/crear-ahorro.sql", "r", encoding="utf-8") as archivo:
            consulta = archivo.read()
        cursor.execute(consulta)
        cursor.connection.commit()
        cursor.close()

    @classmethod
    def borrar_tabla(cls):
        """Ejecuta el script SQL para borrar la tabla planes_ahorro."""
        cursor = cls.obtener_cursor()
        with open("sql/borrar-ahorro.sql", "r", encoding="utf-8") as archivo:
            consulta = archivo.read()
        cursor.execute(consulta)
        cursor.connection.commit()
        cursor.close()

    @classmethod
    def insertar(cls, plan: PlanAhorro):
        """Inserta una instancia de PlanAhorro en la base de datos."""
        cursor = cls.obtener_cursor()
        consulta = """
            INSERT INTO planes_ahorro (id_plan, nombre_meta, meta, tasa_interes, periodos, abono_extra, cuota_mensual)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(consulta, (
            plan.id_plan, plan.nombre_meta, plan.meta, 
            plan.tasa_interes, plan.periodos, plan.abono_extra, plan.cuota_mensual
        ))
        cursor.connection.commit()
        cursor.close()

    @classmethod
    def buscar_por_id(cls, id_plan: str) -> PlanAhorro | None:
        """Consulta un plan de ahorro por su id_plan (SELECT) y retorna la instancia mapeada."""
        cursor = cls.obtener_cursor()
        consulta = """
            SELECT id_plan, nombre_meta, meta, tasa_interes, periodos, abono_extra, cuota_mensual
            FROM planes_ahorro WHERE id_plan = %s
        """
        cursor.execute(consulta, (id_plan,))
        fila = cursor.fetchone()
        cursor.close()
        
        if fila is None:
            return None

        return PlanAhorro(
            id_plan=fila[0],
            nombre_meta=fila[1],
            meta=float(fila[2]),
            tasa_interes=float(fila[3]),
            periodos=int(fila[4]),
            abono_extra=float(fila[5]),
            cuota_mensual=float(fila[6])
        )