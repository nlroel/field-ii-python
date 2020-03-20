try:
    import matlab.engine
except ImportError:
    pass
from . import MatlabEngine


class EnginePool:
    def __init__(self):
        # session_names = matlab.engine.find_matlab()
        # self.engines = list(map(MatlabEngine, session_names))
        engines = []
        for i in range(6):
            engines.append(matlab.engine.start_matlab("-nodesktop -nojvm -nosplash"))
        self.engines = engines


    def need(self, n):
        if len(self.engines) < n:
            raise EnvironmentError("Not Found Enough MATLAB Sessions! {0}/{1}"
                                   .format(len(self.engines), n))
        return self.engines[:n]

engine_pool = EnginePool()
