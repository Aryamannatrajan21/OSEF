

class RuntimeCorrelations:
    @staticmethod
    def get_rules():
        return [
            # Runtime.Process RUNS_ON Infrastructure.Container
            # Runtime.Request EXECUTES Software.Function
            # Runtime.Trace OBSERVES Architecture.Component
            # Runtime.Event GENERATED_BY Software.Function
            # Runtime.Session USES Infrastructure.Service
        ]
