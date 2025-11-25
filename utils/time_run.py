import time
from support import logger
def log_time(fn):
	def inner(*args, **kwargs):
		tnow = time.time()
		out = fn(*args, **kwargs)
		te = time.time()
		took = te - tnow
		
		if took <= .000_001:
			logger.info(f"{fn.__name__} ran in {took*1_000_000_000:.3f} ns")
		elif took <= .001:
			logger.info(f"{fn.__name__} ran in {took*1_000_000:.3f} μs")
		elif took <= 1:
			logger.info(f"{fn.__name__} ran in {took*1_000:.3f} ms")
		elif took <= 60:
			logger.info(f"{fn.__name__} ran in {took:.2f} s")
		elif took <= 3600:
			logger.info(f"{fn.__name__} ran in {(took)/60:.2f} m")		
		else:
			logger.info(f"{fn.__name__} ran in {(took)/3600:.2f} h")
		return out
	return inner