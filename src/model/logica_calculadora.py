META_MINIMA = 0
TASA_INTERES_MINIMA = 0
MINIMO_PERIODOS = 0
ABONO_EXTRA_MINIMO = 0

class CalculadoraAhorro:
    
    # Clase para calcular la cuota de ahorro.

    def __init__(self, meta: float, tasa_interes: float, periodos: float, abono_extra: float = 0):
        self.meta: float = meta
        self.tasa_interes: float = tasa_interes
        self.periodos: float = periodos
        self.abono_extra: float = abono_extra
        
    def calcular_cuota(self) -> float:
        
        periodos = int(self.periodos)
        cuota = (self.meta - self.abono_extra) * self.tasa_interes / ((1 + self.tasa_interes) ** periodos - 1)
        return cuota
        
class MetaInvalida(Exception):
    """Excepcion que se dispara cuando la meta es menor o igual que cero"""
    def __init__(self):
        super().__init__("La meta de ahorro (M) debe ser mayor que cero")
    
class TasaInteresInvalida(Exception):
    """Excepcion que se dispara cuando la tasa de interes es menor o igual a cero"""
    def __init__(self):
        super().__init__("La tasa de interés (tasa_interes) debe ser mayor que cero")
    
class PeriodosInvalidos(Exception):
    """Excepcion que se dispara cuando los periodos es menor o igual a cero"""
    def __init__(self):
        super().__init__("El número de periodos (periodos) debe ser un entero positivo")
    
class AbonoExtraInvalido(Exception):
    """Excepcion que se dispara cuando el abono extra es menor a cero"""
    def __init__(self):
        super().__init__("El abono extra debe ser menor que la meta de ahorro ")
        
    def verificar_meta(self):
        
        if self.meta <= META_MINIMA:
            raise MetaInvalida()
        
    def verificar_tasa_interes(self):
        
        if self.tasa_interes <= TASA_INTERES_MINIMA:
            raise TasaInteresInvalida()
        
    def verificar_periodos(self):
        
        if self.periodos <= MINIMO_PERIODOS or self.periodos != int(self.periodos):
            raise PeriodosInvalidos()
        
    def verificar_abono_extra(self):
        
        if self.abono_extra < ABONO_EXTRA_MINIMO or self.abono_extra >= self.meta:
            raise AbonoExtraInvalido()
            


def generar_tabla_acumulacion(meta: float, tasa_interes: float, periodos: float, abono_extra: float = 0) -> list:
  
    cuota = CalculadoraAhorro(meta, tasa_interes, periodos, abono_extra).calcular_cuota()
    periodos = int(periodos)

    tabla = []
    SALDO_INICIAL = 0.0
    for periodo in range(1, periodos + 1):
        interes = SALDO_INICIAL * tasa_interes
        abono_extra = abono_extra if periodo == periodos else 0.0
        saldo_final = SALDO_INICIAL + cuota + interes + abono_extra

        tabla.append({
            "periodo": periodo,
            "SALDO_INICIAL": SALDO_INICIAL,
            "cuota": cuota,
            "interes_ganado": interes,
            "abono_extra": abono_extra,
            "saldo_final": saldo_final,
        })

        SALDO_INICIAL = saldo_final

    return tabla


def calcular_totales(tabla: list) -> dict:

    total_cuotas = sum(fila["cuota"] for fila in tabla)
    total_interes = sum(fila["interes_ganado"] for fila in tabla)
    total_abono_extra = sum(fila["abono_extra"] for fila in tabla)
    saldo_final = tabla[-1]["saldo_final"] if tabla else 0.0

    return {
        "total_cuotas": total_cuotas,
        "total_interes": total_interes,
        "total_abono_extra": total_abono_extra,
        "total_aportado": total_cuotas + total_abono_extra,
        "saldo_final": saldo_final,
    }
