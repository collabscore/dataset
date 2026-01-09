
import sys, os
import argparse
import json
from pathlib import Path

sys.path.append("../lib")
sys.path.append("../lib/musicdiff")

# Music analysis module
import converter21
import music21 as m21
import musicdiff as mdiff

from musicdiff.m21utils import DetailLevel
from musicdiff.annotation import AnnScore
from musicdiff.comparison import Comparison
from musicdiff.visualization import Visualization

OUT_DIR="results"
PREDICTED_DIR="predicted"
GROUND_TRUTH_DIR="ground_truth"

def main(argv=None):
	"""
	  Utilitaire de comparaison de partitions numérisées
	  
	  Légèrement adapté du code musicdiff de Francesco Foscarion / Greg Chapman 
	"""

	# Comment out this line to go back to music21's built-in Humdrum/MEI importers.
	converter21.register()

	current_path = os.path.dirname(os.path.abspath(__file__))
	out_dir = os.path.join(current_path, OUT_DIR)

	# On accepte des arguments
	parser = argparse.ArgumentParser(description='Diff utility')
	parser.add_argument('-s', '--score', dest='score',
                   help='Name of the score file')
	parser.add_argument('-a', '--action', dest='action', required=True,
                   help="Action: 'single' or 'multiple' (score(s))")
	args = parser.parse_args()
	
	if args.action == "single":
		
		if args.score is None:
			sys.exit ("You must provide a file name")
		compare_single_score (args.score)
	elif args.action == "multiple":
		compare_multiple_scores ()
	else:
		print (f"Unknown action {args.action}")

	return

def compare_single_score(score_name):
	"""
	   Compares a predicted score (in predicted)
	   and a griund truth (in ground_truth)
	"""
	predicted_path = f"predicted/{score_name}"
	ground_truth_path = f"ground_truth/{score_name}"
	
	if not os.path.exists(predicted_path):
		sys.exit (f"File {predicted_path}  does not exist. Please check.")
	if not os.path.isfile(predicted_path):
		sys.exit (f"{predicted_path} is not a file. Please check.")
	if not os.path.exists(ground_truth_path):
		sys.exit (f"{ground_truth_path}  does not exist. Please check.")
		
	try:
		scpath = Path(score_name)
	except Exception:  # pylint: disable=broad-exception-caught
		sys.exit(f'({score_name}) is not a valid path.')
		
	# Good enough for the time being
	detail= DetailLevel.NoteStaffPosition | DetailLevel.Signatures
	
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
	for diff in diff_list:
		oplist.append({"op": diff[0], "cost": diff[3]})
	report = {"cost": _cost, "nb_diffs": len(diff_list), 
					"operations": oplist}

	outrep = os.path.join (OUT_DIR, f"{scpath.stem}_report.json")
	with open(outrep, "w")  as rep:		
		json.dump (report, rep, indent=2 )

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

def compare_multiple_scores():
	"""
	   Compares a predicted score (in predicted)
	   and a ground truth (in ground_truth)
	"""
	
	# Good enough for the time being
	detail= DetailLevel.NotesAndRests

	mdiff.diff_ml_training("predicted", "ground_truth", 
				"results", detail=detail)

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

if __name__ == "__main__":
	main()