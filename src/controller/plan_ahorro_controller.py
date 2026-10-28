import sys
sys.path.append(".")
sys.path.append("src")

import psycopg2
from model.plan_ahorro import PlanAhorro
import secret_config

class PlanAhorroNoEncontrado(Exception):
    """Se genera cuando el método buscar no encuentra un plan de ahorro en la base de datos."""

class PlanAhorroYaExiste(Exception):
    """Se genera cuando se intenta insertar un plan con un identificador ya existente."""

class ErrorBaseDatos(Exception):
    """Se genera cuando ocurre un error de comunicación o ejecución en la base de datos."""

class PlanAhorroController:

    @classmethod
    def obtener_cursor(cls):
        """Crea la conexión a la base de datos PostgreSQL usando secret_config."""
        try:
            conexion = psycopg2.connect(
                database=secret_config.PGDATABASE,
                user=secret_config.PGUSER,
                password=secret_config.PGPASSWORD,
                host=secret_config.PGHOST,
                port=secret_config.PGPORT
            )
            return conexion.cursor()
        except psycopg2.OperationalError:
            raise ErrorBaseDatos("No fue posible conectar con el servidor de base de datos. Verifique que PostgreSQL esté iniciado y la configuración sea correcta.")
        except Exception:
            raise ErrorBaseDatos("Error al inicializar la conexión con la base de datos.")

    @classmethod
    def crear_tabla(cls):
        """Ejecuta el script SQL para crear la tabla planes_ahorro."""
        try:
            cursor = cls.obtener_cursor()
            with open("sql/crear-ahorro.sql", "r", encoding="utf-8") as archivo:
                consulta = archivo.read()
            cursor.execute(consulta)
            cursor.connection.commit()
            cursor.close()
        except ErrorBaseDatos:
            raise
        except Exception as e:
            raise ErrorBaseDatos(f"Error al crear las tablas en la base de datos: {e}")

    @classmethod
    def borrar_tabla(cls):
        """Ejecuta el script SQL para borrar la tabla planes_ahorro."""
        try:
            cursor = cls.obtener_cursor()
            with open("sql/borrar-ahorro.sql", "r", encoding="utf-8") as archivo:
                consulta = archivo.read()
            cursor.execute(consulta)
            cursor.connection.commit()
            cursor.close()
        except ErrorBaseDatos:
            raise
        except Exception as e:
            raise ErrorBaseDatos(f"Error al borrar las tablas en la base de datos: {e}")

    @classmethod
    def insertar(cls, plan: PlanAhorro):
        """Inserta una instancia de PlanAhorro en la base de datos."""
        try:
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
        except psycopg2.IntegrityError:
            raise PlanAhorroYaExiste(f"Ya existe un plan de ahorro registrado con el ID '{plan.id_plan}'.")
        except ErrorBaseDatos:
            raise
        except Exception as e:
            raise ErrorBaseDatos(f"Error al insertar el plan en la base de datos.")

    @classmethod
    def buscar_por_id(cls, id_plan: str) -> PlanAhorro:
        """Consulta un plan de ahorro por su id_plan (SELECT) y retorna la instancia mapeada."""
        try:
            cursor = cls.obtener_cursor()
            consulta = """
                SELECT id_plan, nombre_meta, meta, tasa_interes, periodos, abono_extra, cuota_mensual
                FROM planes_ahorro WHERE id_plan = %s
            """
            cursor.execute(consulta, (id_plan,))
            fila = cursor.fetchone()
            cursor.close()
            
            if fila is None:
                raise PlanAhorroNoEncontrado(f"El plan de ahorro con ID '{id_plan}' no existe en la base de datos")

            return PlanAhorro(
                id_plan=fila[0],
                nombre_meta=fila[1],
                meta=float(fila[2]),
                tasa_interes=float(fila[3]),
                periodos=int(fila[4]),
                abono_extra=float(fila[5]),
                cuota_mensual=float(fila[6])
            )
        except (PlanAhorroNoEncontrado, ErrorBaseDatos):
            raise
        except Exception as e:
            raise ErrorBaseDatos(f"Error al consultar el plan en la base de datos.")
