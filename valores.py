DEPENDENCIAS = {
    "casa": [],
    "pozo": [],
    "almacen": ["casa", "pozo"],
    "escuela": ["casa", "pozo"],
    "fabrica": ["almacen", "escuela"],
    "comisaria": ["escuela", "casa"],
    "mercado": ["almacen", "fabrica", "comisaria"],
    "teatro": ["escuela", "bar"],
    "bar": [],
    "tienda": ["mercado"]
}
# dinero, población, madera, comida
RECURSOS = {
    "casa": [10, 0, 0]
}