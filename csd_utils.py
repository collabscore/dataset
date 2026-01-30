# ------------------------------------------------------------------------------
# Purpose:	   Run comparison between encoded music score, at an individual or collection level
#
# Authors:	   Philippe Rigaux <philippe.rigaux@cnam.fr>
#
# Copyright:	 (c) 2026- Philippe Rigaux
# License:	   Creative commons CC BY-NC-SA 4.0, see LICENSE.md
# ------------------------------------------------------------------------------

import sys, os
import argparse
import json
from pathlib import Path


# Music analysis modules
import converter21
import music21 as m21
import musicdiff as mdiff

from musicdiff.m21utils import DetailLevel
from musicdiff.annotation import AnnScore, AnnNote, AnnMeasure
from musicdiff.comparison import Comparison
from musicdiff.visualization import Visualization

# Rredefined dirs
OUT_DIR="results"
PREDICTED_DIR="predicted"
GROUND_TRUTH_DIR="ground_truth"

SINGLE_SCORE_ACTION="single"
ALL_SCORES_ACTION="all" 
BUILD_FULL_REPORT="report" 
ACTIONS = [SINGLE_SCORE_ACTION,ALL_SCORES_ACTION,BUILD_FULL_REPORT]

def main(argv=None):
	"""
	Slightly adapted from the musicdiff code by Francesco Foscarion / Greg Chapman 
	"""

	# Use the converted 21 MEI 
	converter21.register()

	current_path = os.path.dirname(os.path.abspath(__file__))
	out_dir = os.path.join(current_path, OUT_DIR)

	# Script args
	parser = argparse.ArgumentParser(description='Diff utility')
	parser.add_argument('-s', '--score', dest='score',
				   help='Name of the score file')
	parser.add_argument('-a', '--action', 
			dest='action', choices=ACTIONS,
			default=SINGLE_SCORE_ACTION,
			help="Action: 'single' or 'all' (score(s))")

	parser.add_argument("-d", "--details", default=["allobjects"],
			nargs="*",
			choices=["decoratednotesandrests", "otherobjects",
			"allobjects",  "style", "metadata", "voicing", 
			"notesandrests", "beams", "tremolos", "ornaments",
			"articulations", "ties", "slurs", "signatures",
			"directions", "barlines", "staffdetails",
			"chordsymbols", "ottavas", "arpeggios", "lyrics"],
		help="included details (can include multiple details)"
		)


	args = parser.parse_args()
	
	# Determine the combination of details
	detail: int = DetailLevel.Default
	if args.details:
		detail = 0
		for det in args.details:
			# combos
			if det == "decoratednotesandrests":
				detail |= DetailLevel.DecoratedNotesAndRests
			elif det == "otherobjects":
				detail |= DetailLevel.OtherObjects
			elif det == "allobjects":
				detail |= DetailLevel.AllObjects
			# bits not in any combo
			elif det == "style":
				detail |= DetailLevel.Style
			elif det == "voicing":
				detail |= DetailLevel.Voicing
			elif det == "metadata":
				detail |= DetailLevel.Metadata
			# bits in the DecoratedNotesAndRests combo
			elif det == "notesandrests":
				detail |= DetailLevel.NotesAndRests
			elif det == "beams":
				detail |= DetailLevel.Beams
			elif det == "tremolos":
				detail |= DetailLevel.Tremolos
			elif det == "ornaments":
				detail |= DetailLevel.Ornaments
			elif det == "articulations":
				detail |= DetailLevel.Articulations
			elif det == "ties":
				detail |= DetailLevel.Ties
			elif det == "slurs":
				detail |= DetailLevel.Slurs

			# bits in the OtherObjects combo
			elif det == "signatures":
				detail |= DetailLevel.Signatures
			elif det == "directions":
				detail |= DetailLevel.Directions
			elif det == "barlines":
				detail |= DetailLevel.Barlines
			elif det == "staffdetails":
				detail |= DetailLevel.StaffDetails
			elif det == "chordsymbols":
				detail |= DetailLevel.ChordSymbols
			elif det == "ottavas":
				detail |= DetailLevel.Ottavas
			elif det == "arpeggios":
				detail |= DetailLevel.Arpeggios
			elif det == "lyrics":
				detail |= DetailLevel.Lyrics

	if args.action == SINGLE_SCORE_ACTION:
		if args.score is None:
			sys.exit ("You must provide a file name")
		compare_single_score (args.score, detail)
	elif args.action == ALL_SCORES_ACTION:
		compare_collection (detail)
	elif args.action == BUILD_FULL_REPORT:
		build_full_report ()
	else:
		print (f"Unknown action {args.action}")

	return

def compare_single_score(score_name, detail):
	"""
	   Compares a predicted score (in predicted)
	   and a ground truth (in ground_truth)
	"""
	predicted_path = f"predicted/{score_name}"
	ground_truth_path = f"ground_truth/{score_name}"
	
	if not os.path.exists(predicted_path):
		raise Exception (f"File {predicted_path}  does not exist. Please check.")
	if not os.path.isfile(predicted_path):
		raise Exception (f"{predicted_path} is not a file. Please check.")
	if not os.path.exists(ground_truth_path):
		raise Exception (f"{ground_truth_path}  does not exist. Please check.")
		
	try:
		scpath = Path(score_name)
	except Exception:  # pylint: disable=broad-exception-caught
		sys.exit(f'({score_name}) is not a valid path.')
		
	
	# Get the file name without extension
	print(f"Comparing input files {predicted_path} and {ground_truth_path} ")

	predicted_score = m21.converter.parse(predicted_path, forceSource=True)
	ground_score = m21.converter.parse(ground_truth_path, forceSource=True)

	# scan each score, producing an annotated wrapper
	annotated_predicted: AnnScore = AnnScore(predicted_score, detail)
	annotated_ground: AnnScore = AnnScore(ground_score, detail)
	
	diff_list, _cost = Comparison.annotated_scores_diff(annotated_predicted, 
														annotated_ground)

	oplist = []
	score_report = MdiffScoreReport(score_name)
	
	for diff in diff_list:
		if isinstance(diff[1], AnnNote):
			print (f"Diff object is a note")
		if isinstance(diff[1], AnnMeasure):
			print (f"Diff object is a measure")
		
		op = MdiffOp (diff[0], diff[1], diff[2], diff[3])		
		score_report.add (op)

	outrep = os.path.join (OUT_DIR, f"{scpath.stem}_report.json")
	with open(outrep, "w")  as rep:		
		json.dump (score_report.to_dict(), rep, indent=2 )

	Visualization.mark_diffs(predicted_score, ground_score, diff_list)
	
	# Generate and store the MusicXML file and PDF file
	outpdf1 = os.path.join (OUT_DIR, f"{scpath.stem}_predicted_diff.pdf")
	predicted_score.write("musicxml.pdf", makeNotation=False, fp=outpdf1)
	outpdf2 = os.path.join (OUT_DIR, f"{scpath.stem}_ground_diff.pdf")
	ground_score.write("musicxml.pdf", makeNotation=False, fp=outpdf2)

	print (f"See files ({outpdf1} and {outpdf2})")
	print (f"Indicators and operations list is in {outrep}")

	return
	
	mdiff.diff(predicted_score, ground_score, outpath1, outpath2,
			print_omr_ned_output=True, 
			print_text_output=True, 
			detail=detail)

def compare_collection():
	"""
	   Loop on all scores and compute diffs
	"""
	with open("dataset.json") as json_data:
		dataset = json.load (json_data)
	
		# Loop on the scores, show the results
		for score in dataset["list_opus"]:
			file_name = f"{score['ref']}.mei"
			print (f"\n\nCompute DIFFS for score {score['title']} (file {file_name})")
			try:
				compare_single_score (file_name)
			except Exception as e:
				print (f"Exception met for score {score['title']}: {e}")

def ml_training():
	"""
	   Run the ML training function
	"""
	
	# Good enough for the time being
	detail= DetailLevel.NotesAndRests

	mdiff.diff_ml_training("predicted", "ground_truth", 
				"results", detail=detail)


def build_full_report():
	"""
	  Build HTML and other file summarizing the comparison results
	"""
	report_name = "full_report.html"
	# First load the dataset.json 
	with open("dataset.json") as json_data:
		dataset = json.load (json_data)
	with open(report_name, "w") as res_file:
		res_file.write (f"<table border='1'>")
		res_file.write ("<tr>")
		res_file.write (f"<th>Ref</th><th>Title</th><th>Images</th>")
		res_file.write (f"<th>Nb diffs</th>")
		res_file.write (f"</tr>")

		# Loop on the scores, show the results
		for score in dataset["list_opus"]:
			res_file.write (f"<tr>")
			res_file.write (f"<td>{score['ref']}</td>")
			res_file.write (f"<td>{score['title']}</td>")
			res_file.write (f"<td><a target='_blank' href='{score['iiif_link']}'>link</a></td>")

			# Is there a result file ?
			report_file =f"results/{score['ref']}_report.json"
			if os.path.exists(report_file):
				print(f"\tResult file exists for score {score['ref']}.")
				with open(report_file, "r") as report_file:
					report = MdiffScoreReport.from_dict(json.load (report_file))
					
					res_file.write (f"<td>{report['nb_diffs']}</td>")
			res_file.write (f"</tr>")
		
		res_file.write (f"</table>")

	print (f"\nDone. Report stored in {report_name}")

def old_decomposed_code():
		
	# scan each score, producing an annotated wrapper
	annotated_score1: AnnScore = AnnScore(score1, detail)
	annotated_score2: AnnScore = AnnScore(score2, detail)
	
	diff_list, _cost = Comparison.annotated_scores_diff(annotated_score1, 
														annotated_score2)

	Visualization.mark_diffs(score1, score2, diff_list)


	# Generate and store the MusicXML file and PDF file
	outpath = os.path.join (OUT_DIR, f"{scpath.stem}_diff.xml")
	score1.write ("musicxml", outpath)
	outpdf = os.path.join (OUT_DIR, f"{scpath.stem}_diff.pdf")
	score1.write("musicxml.pdf", makeNotation=False, fp=outpdf)

	#outpath2 = os.path.join (OUT_DIR, f"{scpath2.stem}_diff.xml")
	#score2.write ("musicxml", outpath2)
	#outpdf2 = os.path.join (OUT_DIR, f"{scpath2.stem}_diff.pdf")
	#score2.write("musicxml.pdf", makeNotation=False, fp=outpdf2)

	oplist = []
	for diff in diff_list:
		oplist.append({"op": diff[0], "cost": diff[3]})
	report = {"cost": _cost, "nb_diffs": len(diff_list), "operations": oplist}

	outrep = os.path.join (OUT_DIR, f"{scpath.stem}_report.json")
	with open(outrep, "w")  as rep:		
		json.dump (report, rep, indent=2 )
		
	print (f"See files ({outpath}, {outpdf})")
	print (f"Indicators and operations list is in {outrep}")

###########
#
# Classes that wrap musicdiff operations
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
					cost) :
		self.name = name
		self.first_annot_obj = first_annot_obj
		self.second_annot_obj = second_annot_obj
		self.cost = cost
		
	def to_dict(self):
		return {
			"op_name": self.name,
			"first_annot_obj": str(self.first_annot_obj),
			"second_annot_obj": str(self.second_annot_obj),
			"cost": self.cost
			}

	def __repr__(self):
		return f'Op ({self.name}. ({self.first_annot_obj}, {self.second_annot_obj}). Cost: {self.cost}'

class MdiffScoreReport():
	"""
		List of operations found in a Diff measurement 
		over one score
	"""
	def __init__(self, score_ref) :
		self.score_ref = score_ref
		self.global_cost = 0
		
		# The detailed list of operations
		self.detailed_ops = []
		# Operations aggregated on the name
		self.aggr_ops = {}

	def add(self, op):
		self.detailed_ops.append(op)
		
		# Aggregate
		if op.name in self.aggr_ops:
			self.aggr_ops[op.name]["ops"].append(op.to_dict())
		else:
			self.aggr_ops[op.name] = {"ops": [op.to_dict()]}

	def to_dict(self):
		ops_dict = []
		for op in self.detailed_ops:
			ops_dict.append(op.to_dict())
		
		return {
			"score_ref": self.score_ref,
			"global_cost": self.global_cost,
			"nb_diffs": len(self.detailed_ops),
			"aggr_ops": self.aggr_ops
			}
	
	@staticmethod
	def from_dict(dict_report):
		report = MdiffScoreReport (dict_report["score_ref"])
		report.global_cost = dict_report["global_cost"]
		for aggr_op in dict_report["aggr_ops"]:
			for op_name, op_list in aggr_op["ops"]:
				print (f"Found op {op_name}")
		
if __name__ == "__main__":
	main()