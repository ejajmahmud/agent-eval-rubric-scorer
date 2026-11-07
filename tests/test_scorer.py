"""Tests for agent-eval-rubric-scorer."""
import unittest
from agent_eval_rubric_scorer.scorer import AgentEvalRubricScorer


class TestRubricScorer(unittest.TestCase):
    def test_perfect_trajectory(self):
        traj = {"turns": 4, "tool_errors": 0, "goal_met": True, "security_violations": 0}
        rep = AgentEvalRubricScorer.evaluate(traj)
        self.assertEqual(rep.composite_score, 100.0)
        self.assertTrue(rep.to_dict()["passed"])

    def test_failed_security_trajectory(self):
        traj = {"turns": 10, "tool_errors": 2, "goal_met": False, "security_violations": 2}
        rep = AgentEvalRubricScorer.evaluate(traj)
        self.assertFalse(rep.to_dict()["passed"])
        self.assertEqual(rep.safety_score, 0.0)
