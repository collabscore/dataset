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
	
	NOTE_INS = "noteins"
	NOTE_DEL = "notedel"
	DOT_DEL = "dotdel"
	EXTRA_DEL = "extradel"
	EXTRA_INS = "extrains"
	BAR_DEL = "insbar"
	BAR_INS = "delbar"
	
	OPERATIONS = [NOTE_INS,NOTE_DEL,DOT_DEL,EXTRA_DEL,
					EXTRA_INS, BAR_DEL, BAR_INS]
	
	def __init__(self, name, first_annot_obj=None, second_annot_obj=None, 
					cost=0, type="Unknown") :
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

	def detail_line(self, mode='html'):
		latex_format = """<tr><td></td>
							<td></td><td></td>
							<td>{first_obj}</td>
							<td>{second_obj}</td>
							<td>{type}</td>
							<td>{cost}</td>
							</tr>"""

		return latex_format.format(op_name=self.name,
								first_obj=self.first_annot_obj,
								second_obj=self.second_annot_obj,
								type=self.type,
								cost=self.cost)

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
	
	def nb_diffs(self):
		return len (self.ops)
		
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

	@staticmethod
	def detail_line_header(mode='html'):
		return """<tr><th><th>Operation</th><th>Global cost</th>
							<th>First object</th>
							<th>Second object</th>
							<th>Type</th>
							<th>Cost</th>
							</tr>"""

	def detail_line(self, mode='html'):
		latex_format = """<tr><td>{op_name}</td>
							<td>{cost}</td>
							</tr>"""

		return latex_format.format(op_name=self.label,
								cost=self.cost)

class MdiffScoreReport():
	"""
		List of operations found in a Diff measurement 
		over one score
	"""
	DETAILED_REPORT_NAME = "results/{ref}_report.html"
	EMPTY_REPORT_NAME = "results/empty_report.html"

	def __init__(self, score_ref, title, iiif_link) :
		self.score_ref = score_ref
		self.title = title
		self.iiif_link = iiif_link
		self.global_cost = 0
		self.nb_diffs = 0
		# Operations aggregated and indexed by label, inst. of MdiffListOps
		self.aggr_ops = {}
		# Tells whether at least on op has been added
		self.empty_report = True
		
	def add(self, op):
		
		self.global_cost += op.cost
		self.empty_report = False
		self.nb_diffs += 1
		if not op.name in self.aggr_ops:
			self.aggr_ops[op.name] = MdiffListOps(op.name)
		self.aggr_ops[op.name].add(op)

	def details_link (self):
		# Link to a detailed HTML file
		if self.empty_report:
			return self.EMPTY_REPORT_NAME
		else:
			return self.DETAILED_REPORT_NAME.format(ref=self.score_ref)
			
	def to_dict(self):
		ops_dict = {}
		for label, aggr_op in self.aggr_ops.items():
			ops_dict[label] = aggr_op.to_dict()
		
		return {
			"score_ref": self.score_ref,
			"title": self.title,
			"iiif_link": self.iiif_link,
			"global_cost": self.global_cost,
			"nb_diffs": self.nb_diffs,
			"aggr_ops": ops_dict
			}
	
	def op_info(self, label):
		# Get the list of operations for a given labeel
		if label not in self.aggr_ops.keys():
			# Return a list with default values
			return MdiffListOps  (label)
		else:
			return self.aggr_ops[label]
		
	@staticmethod
	def from_dict(dict_report):
		report = MdiffScoreReport (dict_report["score_ref"],
						dict_report["title"],
						dict_report["iiif_link"]
		)
		report.global_cost = dict_report["global_cost"]
		report.nb_diffs = dict_report["nb_diffs"]
		report.empty_report = False
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
							<th>Details</th>
							<th>Nb diffs</th>
							<th>Note ins.</th>
							<th>Note del.</th>
							<th>Dot del.</th>
							<th>Extra del.</th>
							<th>Extra ins.</th>
							<th>Bar del.</th>
							<th>Bar ins.</th>
							</tr>"""
							
	def line(self, mode='html'):
		latex_format = """<tr><td>{ref}</td><td>{title}</td>
		                    <td><a target='_blank' href='{iiif_link}'>link</a></td>
							<td><a target='_blank' href='{details_link}'>{details_link}</a></td>
							<td>{nb_diffs}</td>
							<td>{noteins}</td>
							<td>{notedel}</td>
							<td>{dotdel}</td>
							<td>{extrains}</td>
							<td>{extradel}</td>
							<td>{barins}</td>
							<td>{bardel}</td>
							</tr>"""

		return latex_format.format(ref=self.score_ref, title=self.title,
								iiif_link=self.iiif_link, 
								details_link=self.details_link(),
								nb_diffs = self.nb_diffs,
								noteins=self.op_info(MdiffOp.NOTE_INS).nb_diffs(),
								notedel=self.op_info(MdiffOp.NOTE_DEL).nb_diffs(),
								dotdel=self.op_info(MdiffOp.DOT_DEL).nb_diffs(),
								extrains=self.op_info(MdiffOp.EXTRA_INS).nb_diffs(),
								extradel=self.op_info(MdiffOp.EXTRA_DEL).nb_diffs(),
								barins=self.op_info(MdiffOp.BAR_INS).nb_diffs(),
								bardel=self.op_info(MdiffOp.BAR_DEL).nb_diffs(),
								)

