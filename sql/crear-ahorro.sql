CREATE TABLE planes_ahorro (
    id_plan VARCHAR(50) NOT NULL PRIMARY KEY,
    nombre_meta VARCHAR(100) NOT NULL,
    meta NUMERIC(15, 2) NOT NULL,
    tasa_interes NUMERIC(8, 4) NOT NULL,
    periodos INTEGER NOT NULL,
    abono_extra NUMERIC(15, 2) DEFAULT 0,
    cuota_mensual NUMERIC(15, 2) NOT NULL
);