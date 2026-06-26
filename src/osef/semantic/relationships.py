"""
Semantic Relationship Enricher (Call Graph).
"""

from osef.parser.symbol_table import SymbolTable


class RelationshipEnricher:
    """
    Builds the Call Graph by mapping 'calls' metadata into explicit related_ids.
    """

    def __init__(self, symbol_table: SymbolTable):
        self.symbol_table = symbol_table

    def enrich_calls(self) -> None:
        """
        Maps function/method calls to SymbolTable IDs.
        """
        all_funcs = self.symbol_table.find_by_type(
            "function"
        ) + self.symbol_table.find_by_type("method")

        # Name to Symbol map for fast lookup
        func_map = {f.name: f.id for f in all_funcs}

        for caller in all_funcs:
            calls_str = caller.metadata.get("calls", "")
            if not calls_str:
                continue

            for callee_name in calls_str.split(","):
                if not callee_name:
                    continue
                if callee_name in func_map:
                    target_id = func_map[callee_name]
                    if "CALLS" not in caller.related_ids:
                        caller.related_ids["CALLS"] = []
                    if target_id not in caller.related_ids["CALLS"]:
                        caller.related_ids["CALLS"].append(target_id)
