"""CLI for agent-eval-rubric-scorer."""
import sys
import argparse
from .scorer import AgentEvalRubricScorer


def main():
    parser = argparse.ArgumentParser(description="Agent Eval Rubric Scorer")
    parser.add_argument("--demo", action="store_true", help="Run demonstration")
    args = parser.parse_args()

    if args.demo:
        sample_traj = {
            "turns": 6,
            "tool_errors": 0,
            "goal_met": True,
            "security_violations": 0
        }
        report = AgentEvalRubricScorer.evaluate(sample_traj)
        print("Evaluation Report:")
        import json
        print(json.dumps(report.to_dict(), indent=2))
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
