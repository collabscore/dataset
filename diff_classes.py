# ------------------------------------------------------------------------------
# Purpose:	   Run comparison between encoded music score, at an individual or collection level
#
# Authors:	   Philippe Rigaux <philippe.rigaux@cnam.fr>
#
# Copyright:	 (c) 2026- Philippe Rigaux
# License:	   Creative commons CC BY-NC-SA 4.0, see LICENSE.md
# ------------------------------------------------------------------------------


###########
#
# Classes wrapping musicdiff operations
#
##########

class MdiffOp ():
	""" Description of MDiff operations
		op[0] is a string describing the diff: “extradel”, or “beamedit” or whatever.
		op[1] is the the AnnNote or AnnExtra or AnnVoice or AnnWhatever in the first score (None if the diff is an add)
		op[2] is the AnnNote or AnnExtra or AnnVoice or AnnWhatever in the second score (None if the diff is a delete)
		op[3] is the edit distance for this diff
	"""
	
	INS_NOTE = "noteins"
	DEL_NOTE = "notedel"
	
	OPERATIONS = [INS_NOTE,DEL_NOTE]
	
	def __init__(self, name, first_annot_obj, second_annot_obj, 
					cost, type) :
		self.name = name
		self.first_annot_obj = first_annot_obj
		self.second_annot_obj = second_annot_obj
		self.cost = cost
		self.type = type
		
	def to_dict(self):
		return {
			"label": self.name,
			"first_annot_obj": str(self.first_annot_obj),
			"second_annot_obj": str(self.second_annot_obj),
			"cost": self.cost,
			"type": self.type
			}

	@staticmethod
	def from_dict(op_dict):
		return MdiffOp (op_dict["label"], 
						op_dict["first_annot_obj"], 
						op_dict["second_annot_obj"], 
						op_dict["cost"],
						op_dict["type"]
						)

	def __repr__(self):
		return f'Op ({self.name}. ({self.first_annot_obj}, {self.second_annot_obj}). Cost: {self.cost}'


class MdiffListOps ():
	""" 
		List of operations sharing the same label
	"""
	def __init__(self, label) :
		self.label = label
		self.cost = 0
		# Detailed list of ops, instances of MdiffOp
		self.ops = []
	
	def add (self, op):
		self.cost += op.cost
		self.ops.append(op)
		
	def to_dict(self):
		ops_dict = []
		for op in self.ops:
			ops_dict.append(op.to_dict())
		
		return {
			"label": self.label,
			"cost": self.cost,
			"nb_diffs": len (self.ops),
			"ops": ops_dict
			}
	
	@staticmethod
	def from_dict(label, dict_list_ops):
		ops_list = MdiffListOps (label)
		ops_list.cost = dict_list_ops["cost"]
		for dict_op in dict_list_ops["ops"]:
			ops_list.add (MdiffOp.from_dict(dict_op))
		return ops_list

class MdiffScoreReport():
	"""
		List of operations found in a Diff measurement 
		over one score
	"""
	def __init__(self, score_ref) :
		self.score_ref = score_ref
		self.global_cost = 0
		self.nb_diffs = 0
		# Operations aggregated and indexed by label, inst. of MdiffListOps
		self.aggr_ops = {}

	def add(self, op):
		
		self.global_cost += op.cost
		self.nb_diffs += 1
		if not op.name in self.aggr_ops:
			self.aggr_ops[op.name] = MdiffListOps(op.name)
		self.aggr_ops[op.name].add(op)

	def to_dict(self):
		ops_dict = {}
		for label, aggr_op in self.aggr_ops.items():
			ops_dict[label] = aggr_op.to_dict()
		
		return {
			"score_ref": self.score_ref,
			"global_cost": self.global_cost,
			"nb_diffs": self.nb_diffs,
			"aggr_ops": ops_dict
			}
	
	def get_ops_list(self, label):
		# Get a list of operations 
		if label not in self.aggr_ops.keys():
			print (f"Warning : attemps to get a non existing ops with label {label}")
			return None 
		else:
			return self.aggr_ops[label]
		
	@staticmethod
	def from_dict(dict_report):
		report = MdiffScoreReport (dict_report["score_ref"])
		report.global_cost = dict_report["global_cost"]
		report.nb_diffs = dict_report["nb_diffs"]
		for label, aggr_op in dict_report["aggr_ops"].items():
			report.aggr_ops[label] = MdiffListOps.from_dict (label, aggr_op)
		return report
	
	### Latex or HTML formatting. Maybe put somewhere else
	
	@staticmethod
	def table_header(mode='html'):
		return "<table border='1'>"
	@staticmethod
	def table_footer(mode='html'):
		return "</table>"
	
	@staticmethod
	def line_header(mode='html'):
		return """<tr><th>Ref</th><th>Title</th><th>Images</th>
							<th>Nb diffs</th></tr>"""
	@staticmethod
	def line(ref, title, iiif_link, report, mode='html'):
		latex_format = """<tr><td>{ref}</td><td>{title}</td>
		                    <td><a target='_blank' href='{iiif_link}'><link></a></td>
							<td>{nb_diffs}</td></tr>"""
		return latex_format.format(ref=ref, title=title,
								iiif_link=iiif_link, 
								nb_diffs = report.nb_diffs)
