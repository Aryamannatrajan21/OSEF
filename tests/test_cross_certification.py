import os
import sys

# Setup paths
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("reference-plugins/typescript"))

from src.osef.sdk.language.cross_certification import CrossLanguageCertificationEngine
from src.pipeline import TypeScriptPipeline

def test_cross_certification():
    print("🚀 Initializing CrossLanguageCertificationEngine...")
    
    # We load only TS right now to self-validate the engine
    pipelines = {
        "typescript": TypeScriptPipeline()
    }
    
    engine = CrossLanguageCertificationEngine(pipelines)
    
    fixture_dir = "language-fixtures/equivalence/concepts/class"
    matrix_path = f"{fixture_dir}/equivalence_matrix.yaml"
    
    print(f"📄 Validating against Matrix: {matrix_path}")
    report = engine.certify_fixture(fixture_dir, matrix_path)
    
    print("\n=========================================")
    print("🛡️  Cross Language Certification Results 🛡️")
    print(f"Structural Equivalence:  {report.structural_equivalence_score}%")
    print(f"Semantic Equivalence:    {report.semantic_equivalence_score}%")
    print(f"Graph Equivalence:       {report.graph_equivalence_score}%")
    print(f"Pipeline Equivalence:    {report.pipeline_equivalence_score}%")
    print(f"Abstraction Leakage:     {'FAIL' if report.leakage_report.has_leakage else 'PASS (Clean)'}")
    print("=========================================")
    
    if report.is_certified:
        print("✅ SUCCESS: Engine Self-Validation Passed. SDK is constitutionally isolated and ready for Java.")
    else:
        print("❌ FAILURE: Certification did not reach 100%. Check leakage reports.")
        if report.leakage_report.has_leakage:
            print(f"   Leakages found: {report.leakage_report.leaked_artifacts}")
            
if __name__ == "__main__":
    test_cross_certification()
