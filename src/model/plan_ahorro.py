class PlanAhorro:
    """
    Representa una entidad de Plan de Ahorro en la capa de Modelo (ORM manual).
    """
    def __init__(self, id_plan: str, nombre_meta: str, meta: float, 
                 tasa_interes: float, periodos: int, abono_extra: float, cuota_mensual: float):
        self.id_plan = str(id_plan)
        self.nombre_meta = str(nombre_meta)
        self.meta = float(meta)
        self.tasa_interes = float(tasa_interes)
        self.periodos = int(periodos)
        self.abono_extra = float(abono_extra)
        self.cuota_mensual = float(cuota_mensual)

    def is_equal(self, comparar_con) -> bool:
        """Compara la instancia actual con otra instancia de PlanAhorro."""
        assert self.id_plan == comparar_con.id_plan
        assert self.nombre_meta == comparar_con.nombre_meta
        assert round(self.meta, 2) == round(comparar_con.meta, 2)
        assert round(self.tasa_interes, 4) == round(comparar_con.tasa_interes, 4)
        assert self.periodos == comparar_con.periodos
        assert round(self.abono_extra, 2) == round(comparar_con.abono_extra, 2)
        assert round(self.cuota_mensual, 2) == round(comparar_con.cuota_mensual, 2)
        return True