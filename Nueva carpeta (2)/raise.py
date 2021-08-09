#try:
#    raise NameError('Errorrr')
#except NameError:
#    print ('Ocurrio una excepcion')\
#        raise


def func():
    raise IOError

try:
    func()
except IOError as exc:
    raise RuntimeError('No se puede abrir la BD') from exc

