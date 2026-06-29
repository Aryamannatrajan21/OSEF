import cProfile
import pstats
from osef.core.pipeline import PipelineEngine

engine = PipelineEngine(".")
cProfile.run("engine.build()", "profile_results")
p = pstats.Stats("profile_results")
p.sort_stats("cumulative").print_stats(30)
