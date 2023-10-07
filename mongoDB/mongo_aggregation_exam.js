db.grades.aggregate([
	{
		$addFields: {
			tmp_scores: {
				$filter: {
					input: "$scores",
					as: "scores_var",
					cond: {
						$or: [
							{$eq: ["$$scores_var.type", 'exam']},
							{$eq: ["$$scores_var.type", 'quiz']}
						]
					}
				}
			}
		}
	},
	{
		$unset: ["scores", "student_id"]
	},
	{
		$unwind: "$tmp_scores"
	},
	{
		$group: {
			_id: "$class_id",
			exam_scores: {
				$push: {
					$cond: {
						if: {
							$eq: ["$tmp_scores.type", 'exam']
						},
						then: "$tmp_scores.score",
						else: "$$REMOVE"
					}
				}
			},
			quiz_scores: {
				$push: {
					$cond: {
						if: {
							$eq: ["$tmp_scores.type", 'quiz']
						},
						then: "$tmp_scores.score",
						else: "$$REMOVE"
					}
				}
			}
		}
	},
	{
		$project: {
			_id: 1,
			scores: {
				$objectToArray: {
					exam: {
						$avg: "$exam_scores"
					},
					quiz: {
						$avg: "$quiz_scores"
					}
				}
			}
		}
	},
	{
		$sort: {
			_id: -1
		}
	},
	{
		$limit: 5
	}
])